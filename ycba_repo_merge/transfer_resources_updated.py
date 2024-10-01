import connections.API as api
import csv
import json
import sys
import logging

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


def get_rowcount(fp) -> int:
    '''Calculates the number of rows in a CSV file
        
       Parameters:
        fp: A string representation of the input file path

       Returns:
        The number of rows in the input file
    '''
    with open(fp, 'r', encoding='utf8') as input_file:
        return len(list(csv.reader(input_file))) - 1


input_file = "files/ycba_repo_merge/transfers.csv"
output_file = open("files/ycba_repo_merge/transfers_success.csv", 'a', encoding='utf8')
error_file = open("files/ycba_repo_merge/transfers_errors.csv", "a", encoding='utf8')
with open(input_file, 'r', encoding='utf8') as infile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames + ['info'])
    writer.writeheader()
    err_writer = csv.DictWriter(error_file, fieldnames=reader.fieldnames + ['info'])
    err_writer.writeheader()
    row_count = get_rowcount(input_file)
    if api.conn():
        print("connected")
        for row in progress_bar(reader, count=row_count):
            try:
                uri = row['uri']
                record_json = api.client.get(uri).json()
                with open(f"files/ycba_repo_merge/backups/{uri[1:].replace('/','_')}.json", 'a', encoding='utf8') as outfile:
                    json.dump(record_json, outfile, sort_keys=True, indent=4)
                transfer_uri = f"{row['uri']}/transfer?target_repo={row['target_repo']}"
                transfer = api.client.post(transfer_uri)
                row['info'] = transfer.json()
                writer.writerow(row)
            except (api.ArchivesSpaceError) as err:
                print("Aspace Error")
                logging.error(err)
                instructions = input(f'Error! Enter R to retry, S to skip, Q to quit: ')
                if instructions == 'R':
                    logging.debug('Trying again...')
                    transfer = api.client.post(transfer_uri)
                    writer.writerow(transfer)
                elif instructions == 'S':
                    row['info'] = err
                    err_writer.writerow(row)
                    logging.debug('Skipping record...')
                    continue
                elif instructions == 'Q':
                    logging.debug('Exiting on user request...')
                    break
            except api.LoginError as login_err:
                row['info']=(login_err)
                err_writer.writerow(row)
            except Exception as gen_ex:
                row['info'] = gen_ex
                err_writer.writerow(row)
    else:
        print("Connection failed. Are you connected to the VPN?")

