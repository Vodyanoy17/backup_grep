import os
import csv
import argparse
from colorama import Fore, Back, Style
from collections import defaultdict

def read_errors(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        # skip lines that start with ‘#’
        return [item for sublist in reader if not sublist[0].startswith('#') for item in sublist]

def find_errors(log_file, errors):
    error_counts = defaultdict(int)
    error_lines = {}
    with open(log_file, 'r') as file:
        for line in file:
            for error in errors:
                if error in line:
                    error_counts[error] += 1
                    if error not in error_lines:
                        error_lines[error] = line.strip()
    return error_counts, error_lines

def main():
    parser = argparse.ArgumentParser(description='Find errors in log file.')
    parser.add_argument('log_file', type=str, help='The log file to search')
    args = parser.parse_args()

    script_directory = os.path.dirname(__file__)
    print(script_directory)
    file_path = os.path.join(script_directory, 'backup_errors.csv')
    errors = read_errors(file_path)
    found_errors, error_lines = find_errors(args.log_file, errors)

    for error, count in found_errors.items():
        print(Fore.RED + f"Error Message [{error}]\t\tNumber of its occurrences {count}")
        print(Fore.RESET + Back.GREEN + f"Sample line:{error_lines[error]}"+Back.RESET )

if __name__ == "__main__":
    main()



