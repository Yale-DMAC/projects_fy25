#!/usr/bin/python3

import csv
import json
import logging
import os
import sys

# only do this in testing
from rich import print

import requests

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
                    handlers=[logging.FileHandler("log.log", mode='a'),
                              stream_handler])

class LoginError(Exception):

  def __init__(self, status_code, url, username, message=f"Login failed!"):
      self.status_code = status_code
      self.url = url
      self.username = username
      self.message = message
      super().__init__(self.message)

  def __str__(self):
      return f"{self.message} URL: {self.url}, Username: {self.username}, Status code: {self.status_code}"

class ArchivesSpaceError(Exception):
  def __init__(self, uri, status_code, aspace_message, message=f"ArchivesSpace Error!"):
      self.uri = uri
      self.status_code = status_code
      self.aspace_message = aspace_message
      self.message = message
      super().__init__(self.message)

  def __str__(self):
      return f"{self.message} URI: {self.uri}, Status code: {self.status_code}, Message: {self.aspace_message.get('error')}"

def get_rowcount(fp):
    with open(fp, encoding='utf8') as input_file:
        return len(list(csv.reader(input_file))) - 1

def progress_bar(it, count=None, prefix="", size=60, out=sys.stdout):
    # modified this a bit: https://stackoverflow.com/a/34482761
    if count is None:
        count = len(it)
    def show(counter):
        advance = int(size*counter/count)
        percent_done = counter/count
        print("{}{}{} {}/{} {:.2%}".format(prefix, u"█"*advance, "."*(size-advance), counter, count, percent_done), 
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)

def get_data_path(config, data_type):
    if config:
        csv_path = config.get(data_type)
        if csv_path not in (None, ''):
            return csv_path
        else:
            return input(f'Please enter path to {data_type}: ')
    else:
        return input(f'Please enter path to {data_type}: ')

def check_config():
    path_to_this_file = os.path.dirname(os.path.realpath(sys.argv[0]))
    config_path = os.path.join(path_to_this_file, 'config.json')
    if os.path.exists(config_path):
        with open(config_path, encoding='utf8') as config_file:
            return json.load(config_file)

def check_credentials(config):
    if config:
        if (config.get('api_url') in (None, '')) or (config.get('username') in (None, '')) or (config.get('password') in (None, '')):
            return get_login_inputs()
        else:
            return config['api_url'], config['username'], config['password']
    else:
        return get_login_inputs()

def get_login_inputs():
    url = input('Please enter the ArchivesSpace API URL: ')
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')   
    return url, username, password

def start_session(config):
    url, username, password = check_credentials(config)
    session = requests.Session()
    session.headers.update({'Content_Type': 'application/json'})
    auth_request = session.post(f"{url}/users/{username}/login?password={password}")
    if auth_request.status_code == 200:
        print(f'Login successful!: {url}')
        session_token = json.loads(auth_request.text)['session']
        session.headers['X-ArchivesSpace-Session'] = session_token
        return url, session
    else:
        raise LoginError(auth_request.status_code, url, username)

def create_backups(dirpath, uri, record_json):
    with open(f"{dirpath}/{uri[1:].replace('/','_')}.json", 'a', encoding='utf8') as outfile:
        json.dump(record_json, outfile, sort_keys=True, indent=4)

def handle_result(row, record_post):
    if record_post.get('status') == 'Created':
        row['info'] = record_post['uri']
    return row

def handle_error(error, row):
    logging.error(error)
    row['info'] = error
    return row

def get_record(api_url, uri, sesh):
    record = sesh.get(f"{api_url}{uri}")
    if record.status_code == 200:
        return json.loads(record.text)
    else:
        raise ArchivesSpaceError(uri, record.status_code, json.loads(record.text))

def post_record(api_url, uri, sesh, record_json):
    record = sesh.post(f"{api_url}{uri}", json=record_json)
    # what if the text cannot be converted to json? need to make sure it works
    if record.status_code == 200:
        return json.loads(record.text)
    else:
        raise ArchivesSpaceError(uri, record.status_code, json.loads(record.text))

def update_title(record_json, csv_row) -> tuple:
    '''Updates a record title.

       Parameters:
        record_json: The JSON representation of the top container record.
        csv_row['uri']: The URI of the top container record.
        csv_row['title']: The new title.
    '''
    record_json['title'] = csv_row['title']
    return record_json, csv_row['uri']

def main():
    try:
        config = check_config()
        api_url, sesh = start_session(config)
        input_file_path = get_data_path(config, 'input_csv')
        backup_directory = get_data_path(config, 'backup_directory')
        error_file_path = get_data_path(config, 'error_csv')
        output_file_path = f"{input_file_path.replace('.csv', '')}.csv"
        row_count = get_rowcount(input_file_path)
        with open(input_file_path, 'r', encoding='utf8') as infile, open(output_file_path, 'a', encoding='utf8') as outfile, open(error_file_path, 'a', encoding='utf8') as errfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames + ['info'])
            writer.writeheader()
            err_writer = csv.DictWriter(errfile, fieldnames=reader.fieldnames + ['info'])
            err_writer.writeheader()
            for row in progress_bar(reader, count=row_count):
                try:
                    record_json = get_record(api_url, row['uri'], sesh)
                    create_backups(backup_directory, row['uri'], record_json)
                    record_json, uri = update_title(record_json, row)
                    record_post = post_record(api_url, uri, sesh, record_json)
                    row = handle_result(row, record_post)
                    writer.writerow(row)
                except (ArchivesSpaceError, requests.exceptions.RequestException) as err:
                    row = handle_error(err, row)
                    err_writer.writerow(row)
                    instructions = input(f'Error! Enter R to retry, S to skip, Q to quit: ')
                    if instructions == 'R':
                        logging.debug('Trying again...')
                        record_post = post_record(api_url, uri, sesh, record_json)
                    row = handle_result(row, record_post)
                    writer.writerow(row)
                    elif instructions == 'S':
                        logging.debug('Skipping record...')
                        continue
                    elif instructions == 'Q':
                        logging.debug('Exiting on user request...')
                        break
    except LoginError as login_err:
        logging.error(login_err)
    except Exception as gen_ex:
        logging.error(gen_ex)

if __name__ == '__main__':
    main()