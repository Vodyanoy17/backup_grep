import os
import re
import csv
import mmap
import numpy as np
import argparse
import threading
import matplotlib
from tqdm import tqdm
from collections import defaultdict
from datetime import datetime, date
import matplotlib.pyplot as plt, io, base64

def read_errors(file_name):
    """
        Reads errors from a CSV file, skipping lines starting with '#'.
        Args:
            file_name (str): The path to the CSV file.
        Returns:
            List[str]: A list of errors extracted from the CSV file.

    """
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        # skip lines that start with ‘#’
        return [
            item.strip()
            for sublist in reader
            if not sublist[0].startswith("#")
            for item in sublist
        ]

def get_num_lines(file_path):
    """_summary_

    Args:
        file_path (_type_): _description_

    Returns:
        _type_: _description_
    """
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines

def find_errors(log_file, errors, beginning_timestamp, end_timestamp):
    """
    Searches for specified errors within a time range in a log file.

    Args:
        log_file (str): The path to the log file.
        errors (List[str]): List of error strings to search for.
        beginning_timestamp (str): Start timestamp in the format "%m/%d/%y %H:%M".
        end_timestamp (str): End timestamp in the format "%m/%d/%y %H:%M".

    Returns:
        Tuple[Dict[str, int], Dict[str, str]]:
            A tuple containing:
            - A dictionary with error counts.
            - A dictionary with the first line of the log containing each error.
    """
    error_counts = defaultdict(int)
    error_lines = {}

    begin_datetime = datetime.strptime(beginning_timestamp, "%m/%d/%y %H:%M")
    end_datetime = datetime.strptime(end_timestamp, "%m/%d/%y %H:%M")

 
    with open(log_file, "rb") as file:
        match_first = get_first_timestamp(file)
        if match_first:
            timestamp_first_line_str  = match_first.group(0)
            timestamp_first_line = datetime.strptime(timestamp_first_line_str, "%Y-%m-%dT%H:%M:%S")

        match_last = get_last_timestamp(file)
        if match_last:
            timestamp_last_line_str  = match_last.group(0)
            timestamp_last_line = datetime.strptime(timestamp_last_line_str, "%Y-%m-%dT%H:%M:%S")

    with open(log_file, "r") as file:
        # check if two time intervals intersect 
        # timestamp_first_line, timestamp_last_line,  and begin_datetime, end_datetime 
        # (start1 <= end2 and end1 >= start2)
        if (match_last and match_first and (timestamp_first_line <= end_datetime and timestamp_last_line >= begin_datetime))\
            or not match_first or not match_last:
            for _,line in enumerate(tqdm(file,total= get_num_lines(log_file))):
                # fint the timestaml in the line
                match_time = re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", line)
                if match_time:
                    timestamp_str = match_time.group(0)
                    log_datetime = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S")

                # # fast exit option
                # if (match_time and (log_datetime > end_datetime)):
                #     break
                # Check if the error occurred within the timeframe or if the timestamp in the line is invalid.
                if (match_time and (begin_datetime <= log_datetime <= end_datetime))  or not match_time:
                    for error in errors:
                        if error in line:
                            error_counts[error] += 1
                            if error not in error_lines:
                                error_lines[error] = line.strip()
    return error_counts, error_lines

def get_errors_file_path(errors_list_file):
    script_directory = os.path.dirname(__file__)
    #print(script_directory)
    if errors_list_file == "":
        file_path = os.path.join(script_directory, "bckgrep_backup_errors_6.csv")
    else:
        file_path = os.path.join(script_directory, errors_list_file)
    return file_path

# Define a function to find the timestamp using regular expression
def find_timestamp(line):
    return re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", line)

def get_first_timestamp(file):
    _ = file.readline()

        # Read the second line again to get the actual second line
    second_line = file.readline().decode("utf-8")
        # Use regular expression to find the timestamp
    match_start = find_timestamp(second_line)
    return match_start

def get_last_timestamp(file):
    file.seek(-2, 2)

        # Move the cursor to the beginning of the last line
    while file.read(1) != b'\n':
        file.seek(-2, 1)

        # Read the last line
    last_line = file.readline().decode('utf-8')   
    match_end = find_timestamp(last_line)
    # file.seek(0)  # Move back to the beginning of the file
    return match_end

def log_parser(
    log_file,
    beginning_timestamp="1970-01-01T00:00:00",
    end_timestamp="2190-01-01T23:59:59",
    errors_list_file =""
):
    """
    Parses a log file, searches for errors, and generates an HTML log summary.

    Args:
        log_file (str): The path to the log file.
        beginning_timestamp (str): Start timestamp in the format "%Y-%m-%dT%H:%M:%S".
        end_timestamp (str): End timestamp in the format "%Y-%m-%dT%H:%M:%S".

    Returns:
        str: An HTML-formatted log summary containing error information.
    """
    #print(errors_list_file)
    file_path = get_errors_file_path(errors_list_file)
    errors = read_errors(file_path)
    found_errors, error_lines = find_errors(
        log_file,
        errors,
        beginning_timestamp=beginning_timestamp,
        end_timestamp=end_timestamp,
    )
    # Example of the search link
    # https://search.corp.mongodb.com/#q=%22MULTIPLE_CONCURRENT_SNAPSHOTS%22&sort=date%20descending&f:facet-product=[Ops%20Manager]
  
    html_log = get_html(found_errors, error_lines)

    return html_log

lock = threading.Lock()
def get_html(found_errors, error_lines):
    html_log = ""
    plot_url=""

    with lock:
        plot_url = add_plot(found_errors)
    #html_log = f"""<img src="data:image/png;base64,{plot_url}"  style="height:50%; width:auto;>"""

    html_log = f"""<p><img src="data:image/png;base64,{plot_url}"></p>"""

    sorted_errors = {k: v for k, v in sorted(found_errors.items(), key=lambda item: item[1],reverse=True)}

    for error, count in sorted_errors.items():
        search_link = f"""https://search.corp.mongodb.com/#q=%22{error}%22&sort=date%20descending&f:facet-product=[Ops%20Manager]"""
        embeded_link = f"""<a href="{search_link}" target="_blank">{error}</a>"""

        #html_log += f"""<p>Error Message <strong>[{error}]</strong>    Number of its occurrences <strong>{count}</strong><br>"""
        html_log += f"""<p>Error Message <strong>[{embeded_link}]</strong>    Number of its occurrences <strong>{count}</strong><br>"""
        html_log += f"""Sample line:<span style="color:green;">{error_lines[error]}</span></p>"""
    
    return html_log

def add_plot(found_errors):
   
    matplotlib.use('Agg')
    
    # Calculate bar positions
    bar_height = 0.35
    index = np.arange(len(found_errors))

    # Create a bar chart for the first series
    plt.barh(index, found_errors.values(), bar_height)

    plt.ylabel('Error')
    plt.xlabel('Count')
    plt.title('Error Count Bar Chart')
    plt.yticks(index+bar_height/2, found_errors.keys())  # center the y-axis labels
    #plt.legend()

    # Convert plot to PNG image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    
    plot_url = base64.b64encode(img.getvalue()).decode()

    plt.clf()  # Clear the current figure
    plt.close()  # Close the figure window    
    return plot_url

def main():
    parser = argparse.ArgumentParser(description="Find errors in log file.")
    parser.add_argument("log_file", type=str, help="The log file to search")
    args = parser.parse_args()

    log_parser(args.log_file)


if __name__ == "__main__":
    main()
