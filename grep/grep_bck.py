import os
import re
import csv
import argparse
from colorama import Fore, Back, Style
from collections import defaultdict
from datetime import datetime, date

def read_errors(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        # skip lines that start with ‘#’
        return [item for sublist in reader if not sublist[0].startswith('#') for item in sublist]

def find_errors(log_file, errors,  beginning_timestamp, end_timestamp):
    error_counts = defaultdict(int)
    error_lines = {}

    begin_datetime = datetime.strptime(beginning_timestamp, '%m/%d/%y %H:%M')
    end_datetime = datetime.strptime(end_timestamp, '%m/%d/%y %H:%M')


    print(begin_datetime)
    print(end_datetime)
    with open(log_file, 'r') as file:
        for line in file:
            match_time = re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', line)
            if match_time:
                timestamp_str = match_time.group(0)
                log_datetime = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S')

                if begin_datetime <= log_datetime <= end_datetime:
                    for error in errors:
                        if error in line:
                            error_counts[error] += 1
                            if error not in error_lines:
                                error_lines[error] = line.strip()
    return error_counts, error_lines

def log_parser(log_file, beginning_timestamp="1970-01-01T00:00:00", end_timestamp="2190-01-01T23:59:59"):
    script_directory = os.path.dirname(__file__)
    print(script_directory)
    file_path = os.path.join(script_directory, 'backup_errors.csv')
    errors = read_errors(file_path)
    found_errors, error_lines = find_errors(log_file,errors, beginning_timestamp=beginning_timestamp, end_timestamp=end_timestamp)

    for error, count in found_errors.items():
        print(Fore.RED + f"Error Message [{error}]\t\tNumber of its occurrences {count}")
        print(Fore.RESET + Back.GREEN + f"Sample line:{error_lines[error]}"+Back.RESET )


def main():
    parser = argparse.ArgumentParser(description='Find errors in log file.')
    parser.add_argument('log_file', type=str, help='The log file to search')
    args = parser.parse_args()

    log_parser(args.log_file)
    # script_directory = os.path.dirname(__file__)
    # file_path = os.path.join(script_directory, 'backup_errors.csv')
    # errors = read_errors(file_path)
    # found_errors, error_lines = find_errors(args.log_file, errors)

    # for error, count in found_errors.items():
    #     print(Fore.RED + f"Error Message [{error}]\t\tNumber of its occurrences {count}")
    #     print(Fore.RESET + Back.GREEN + f"Sample line:{error_lines[error]}"+Back.RESET )

if __name__ == "__main__":
    main()



