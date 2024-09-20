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
    '''Custom exception to catch ArchivesSpace login errors

       Returns:
        An f-string which contains the status code of the request, the ArchivesSpace base API URL, the username submitted during the login attempt, and the error message

    '''
    def __init__(self, status_code, url, username, message="Login failed!"):
        self.status_code = status_code
        self.url = url
        self.username = username
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} URL: {self.url}, Username: {self.username}, Status code: {self.status_code}"

class ArchivesSpaceError(Exception):
    '''Custom exception to catch ArchivesSpace API call errors

       Returns:
        An f-string which contains the URI of the record on which the error was encountered, the status code of the request, the error message from the ArchivesSpace response, and the generic error message for the exception
    '''
    def __init__(self, uri, status_code, aspace_message, message="ArchivesSpace Error!"):
        self.uri = uri
        self.status_code = status_code
        self.aspace_message = aspace_message
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} URI: {self.uri}, Status code: {self.status_code}, Message: {self.aspace_message.get('error')}"

def get_rowcount(fp) -> int:
    '''Calculates the number of rows in a CSV file
        
       Parameters:
        fp: A string representation of the input file path

       Returns:
        The number of rows in the input file
    '''
    with open(fp, encoding='utf8') as input_file:
        return len(list(csv.reader(input_file))) - 1

def progress_bar(it, count=None, prefix="", size=60, out=sys.stdout):
    '''A simple local progress bar which obviates the need for a third-party
       library such as tqdm. Adapted from this post: https://stackoverflow.com/a/34482761

       Parameters:
        it: The iterator
        count: Optional precalculated row count, for generators
        prefix: Optional prefix message. Default "".
        size: Optional bar size. Default 60.
        out: Where to output the progress bar. Default stdout.
    '''
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

def get_data_path(config, data_type) -> str:
    '''Checks the location of a CSV file. Asks for a path if file is not found.

       Parameters:
        config: The configuration file
        data_type: The path to the CSV file, if not in the config file.

       Returns:
        A string representation of a user-submitted file path

    '''
    if config:
        csv_path = config.get(data_type)
        if csv_path not in (None, ''):
            return csv_path
        else:
            return input(f'Please enter path to {data_type}: ')
    else:
        return input(f'Please enter path to {data_type}: ')

def check_config(file_name='config.json') -> dict:
    '''Checks whether a configration file exists, and if so opens and returns
       the file. Can handle either .json or .yml files.

       Parameters:
        file_name: The configuration file name. Default value 'config.json'

       Returns:
        The loaded configuration data

       Raises:
        FileNotFoundError - if the condiguration file is not found at the specified path
    '''
    # not sure about this - works if I run from file, doesn't work if I run from repl
    path_to_this_file = os.path.dirname(os.path.realpath(sys.argv[0]))
    config_path = os.path.join(path_to_this_file, file_name)
    if os.path.exists(config_path):
        with open(config_path, encoding='utf8') as config_file:
            if file_name.endswith('yml'):
                return yaml.safe_load(config_file)
            elif file_name.endswith('json'):
                return json.load(config_file)
    else:
        raise FileNotFoundError(f"File {config_path} not found")

def check_credentials(config) -> tuple:
    '''Checks the confiration file for login information, asks for user 
       input if not found.

       Parameters:
        config: The configuration file

       Returns:
        A tuple containing credentials from the configuration file or, if configuration data is missing, from user-submitted input
    '''
    if config:
        if (config.get('api_url') in (None, '')) or (config.get('username') in (None, '')) or (config.get('password') in (None, '')):
            return get_login_inputs()
        else:
            return config['api_url'], config['username'], config['password']
    else:
        return get_login_inputs()

def get_login_inputs() -> tuple:
    '''Requests login information from the end user

       Returns:
        A tuple containing user-submitted ArchivesSpace URL, username, and password
    '''
    url = input('Please enter the ArchivesSpace API URL: ')
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')   
    return url, username, password

def start_session(config=None, return_url=True) -> tuple:
    '''Starts an HTTP session, attempts to login to ArchivesSpace API.

       Parameters:
        config: The configuration file

       Returns:
        The base API URL and session key

       Raises:
        LoginError: if the login is unsuccessful
    '''
    url, username, password = check_credentials(config)
    session = requests.Session()
    session.headers.update({'Content_Type': 'application/json'})
    auth_request = session.post(f"{url}/users/{username}/login?password={password}")
    if auth_request.status_code == 200:
        print(f'Login successful!: {url}')
        session_token = json.loads(auth_request.text)['session']
        session.headers['X-ArchivesSpace-Session'] = session_token
        if return_url:
            return url, session
        else:
            return session
    else:
        raise LoginError(auth_request.status_code, url, username)

def create_backups(dirpath, uri, record_json):
    '''Creates a backup of a JSON file prior to update

       Parameters:
        dirpath: The string representation of the backup directory
        uri: The URI of the record to back up
        record_json: The JSON to back up
    '''
    with open(f"{dirpath}/{uri[1:].replace('/','_')}.json", 'a', encoding='utf8') as outfile:
        json.dump(record_json, outfile, sort_keys=True, indent=4)

def handle_error(error, csv_row) -> dict:
    '''Appends the ArchivesSpace error message of a failed update to the 
       input CSV row

       Parameters:
        error: The error message
        csv_row: The row of input data

       Returns:
        CSV row with the error message of the failed update
    '''
    csv_row['info'] = error
    return csv_row

def get_record(api_url, uri, sesh) -> dict:
    '''Makes an HTTP GET request and attempts to return a JSON response

       Parameters:
        api_url: The base URL of the ArchivesSpace API
        uri: The URI of the record to retrieve
        sesh: The HTTP session object

       Returns:
        The JSON response from the ArchivesSpace API

       Raises:
        ArchivesSpaceError: if there is an error getting the record
    '''
    record = sesh.get(f"{api_url}{uri}")
    if record.status_code == 200:
        return json.loads(record.text)
    else:
        raise ArchivesSpaceError(uri, record.status_code, json.loads(record.text))

def post_record(api_url, uri, sesh, csv_row) -> dict:
    '''Makes an HTTP POST request and attempts to return a JSON response

       Parameters:
        api_url: The base URL of the ArchivesSpace API
        uri: The URI of the record to update
        sesh: The HTTP session object
        record_json: The JSON representation of the record to update
        csv_row: The CSV row containing data to update

       Returns:
        The input CSVDict row with the URI of the successfully posted record

       Raises:
        ArchivesSpaceError: if there is an error posting the record
    '''
    record = sesh.post(f"{api_url}{uri}")
    # what if the text cannot be converted to json? need to make sure it works
    if record.status_code == 200:
        result = json.loads(record.text)
        #if result.get('status') == 'Created':
        csv_row['info'] = result['status']
        return csv_row
    else:
        # do something with the row here?
        raise ArchivesSpaceError(uri, record.status_code, json.loads(record.text))

def transfer_resource(csv_row: dict) -> str:
    '''Updates a top container record with barcode.

       Parameters:
        record_json: The JSON representation of the top container record.
        csv_row['uri']: The URI of the top container record.
        csv_row['target_repo']: The barcode of the top container.
    '''
    print(f"{csv_row.get('uri')}/transfer?target_repo={csv_row.get('target_repo')}")
    return f"{csv_row.get('uri')}/transfer?target_repo={csv_row.get('target_repo')}", csv_row.get('uri')


def main():
    try:
        config = check_config()
        api_url, sesh = start_session(config)
        input_file_path = get_data_path(config, 'input_csv')
        backup_directory = get_data_path(config, 'backup_directory')
        output_file_path = f"{input_file_path.replace('.csv', '')}_success.csv"
        error_file_path = f"{input_file_path.replace('.csv', '')}_errors.csv"
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
                    uri, record_json = transfer_resource(row)
                    row = post_record(api_url, uri, sesh, row)
                    writer.writerow(row)
                except (ArchivesSpaceError, requests.exceptions.RequestException) as err:
                    logging.error(err)
                    instructions = input(f'Error! Enter R to retry, S to skip, Q to quit: ')
                    if instructions == 'R':
                        logging.debug('Trying again...')
                        row = post_record(api_url, uri, sesh, record_json, row)
                        writer.writerow(row)
                    elif instructions == 'S':
                        row = handle_error(err, row)
                        err_writer.writerow(row)
                        logging.debug('Skipping record...')
                        continue
                    elif instructions == 'Q':
                        logging.debug('Exiting on user request...')
                        break
    except LoginError as login_err:
        logging.error(login_err)
    except Exception as gen_ex:
        logging.exception(gen_ex)

if __name__ == '__main__':
    main()