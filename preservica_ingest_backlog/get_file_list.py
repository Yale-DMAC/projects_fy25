#!/usr/bin/python3

import csv
import os


def get_file_list():
    target_path = input('Please enter target file list path: ')
    out_fp = input('Please enter path to output CSV: ')
    with open(out_fp, 'w', encoding='utf8') as ofile:
        writer = csv.writer(ofile)
        writer.writerow(['filepath'])
        for dirpath in os.listdir(target_path):
            full_path = os.path.join(target_path, dirpath)
            writer.writerow([full_path, dirpath])
        # for dirpath, dirnames, filenames in os.walk(target_path):
        #     for dirname in dirnames:
        #         full_path = os.path.join(dirpath, dirname)
        #         writer.writerow([full_path])
            # for filename in filenames:
            #    full_path = os.path.join(dirpath, filename)
            #    writer.writerow([full_path])

def compare_files():
    aspace_filenames = input('Please enter path to list of ArchivesSpace filenames: ')
    backlog_file_paths = input('Please enter path to backlog file paths: ')
    output_path = input('Please enter output path: ')
    mismatch_path = input('Please enter mismatch path: ')
    matches = []
    with open(aspace_filenames, 'r', encoding='utf8') as infile_1, open(backlog_file_paths, 'r', encoding='utf8') as infile_2, open(output_path, 'a', encoding='utf8') as outfile, open(mismatch_path, 'a', encoding='utf8') as mismatches:
        filename_reader = csv.reader(infile_1)
        next(filename_reader)
        backlog_reader = csv.reader(infile_2)
        writer = csv.writer(outfile)
        mis_writer = csv.writer(mismatches)
        header_1 = next(backlog_reader)
        header = header_1 + ['uri']
        writer.writerow(header)
        aspace_filename_dict = {row[1]: row[0] for row in filename_reader}
        for row in backlog_reader:
            if row[1] in aspace_filename_dict:
                row.append(aspace_filename_dict.get(row[1]))
                writer.writerow(row)
            elif row[1] not in aspace_filename_dict:
                mis_writer.writerow(row)


def main():
    compare_files()


if __name__ == "__main__":
    main()