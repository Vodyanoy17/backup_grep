import re
import os
import gzip
import shutil
import fnmatch
import tempfile
import webbrowser
import tkinter as tk
import concurrent.futures
from datetime import datetime
from grep_bck import log_parser
from tkhtmlview import HTMLLabel
from tkinter import ttk #, scrolledtext
from tkcalendar import DateEntry #, Calendar, 
from tkinter import filedialog, messagebox# #simpledialog, 

def get_files_list(directory):
    # List to store the matching file names
    matching_files = []

    # Iterate over all the files in the directory
    for filename in os.listdir(directory):
        # Check if the file name starts with 'mms0' and has the extension '.log'
        if fnmatch.fnmatch(filename, 'mms0*.log') or fnmatch.fnmatch(filename, 'mms0*.log.gz'):
            # Check if the file name does not contain 'access', 'migration', or 'startup'
            if all(x not in filename for x in ['access', 'migration', 'startup']):
                if filename.endswith('.gz'):
                    # Create a temporary file to extract the content of the gzipped log file
                    full_path = os.path.join(directory, filename)
                    with tempfile.NamedTemporaryFile(mode='w+t', delete=False) as temp_file:
                        with gzip.open(full_path, 'rt') as gzipped_file:
                            shutil.copyfileobj(gzipped_file, temp_file)
                            #print(temp_file.name)
                            matching_files.append([filename,temp_file.name])
                else:
                    # Get the full path to the file
                    full_path = os.path.join(directory, filename)
                    # Add the file path to the list
                    matching_files.append([filename,full_path])
    return matching_files

def delete_temporary_files(log_files_list):
    for original_name,log_file in log_files_list:
        if original_name.endswith('.gz'):
            try:
                os.remove(log_file)
                print(f"{log_file} has been deleted successfully.")
            except OSError as e:
                print(f"Error: {log_file} - {e}")


def fill_fields_with_default(log_files_dir):
    """_summary_

    Args:
        log_file (_type_): _description_
    """
    global log_files_list

    # read all files to list
    log_files_list = get_files_list(log_files_dir)

    for _,log_file in log_files_list:
        file_data_extract(log_file)


# Define a function to find the timestamp using regular expression
def find_timestamp(line):
    return re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", line)

def file_data_extract(log_file):
    with open(log_file,'rb') as file:
        """
        fill_fields_with_default(log_file): Reads a log file, extracts the timestamps 
        from the second and last lines, and populates the relevant fields with these timestamps.
        """
        # skip the first line with the header
        _ = file.readline()

        # Read the second line again to get the actual second line
        second_line = file.readline().decode("utf-8")
        # Seek to the end of the file
        file.seek(-2, 2)

        # Move the cursor to the beginning of the last line
        while file.read(1) != b'\n':
            file.seek(-2, 1)

        # Read the last line
        last_line = file.readline().decode('utf-8')

        # Use regular expression to find the timestamp
        match_start = find_timestamp(second_line)
        match_end = find_timestamp(last_line)
    
        current_date = start_date_entry.get_date()
        current_time = start_time_entry.get()

        if match_start:

            timestamp_str_1 = match_start.group(0)
            timestamp_1 = datetime.strptime(timestamp_str_1, "%Y-%m-%dT%H:%M:%S")

            # Check if the current values exist
            if current_date and current_time:
                # Assume current_date and current_time are the current values in the entries
                current_timestamp = datetime.strptime(current_time, "%H:%M")
                # Convert current date and time to datetime for comparison
                current_datetime = datetime.combine(current_date, current_timestamp.time())

                # Check if the new timestamp is less than the current one
                if timestamp_1 < current_datetime:
                    # Populate the start_date_entry, start_time_entry, and other relevant fields with default values
                    start_date_entry.set_date(timestamp_1.date())
                    start_time_entry.set(timestamp_1.strftime("%H:%M"))
            else:
                # If the current values do not exist, set them to the new values
                start_date_entry.set_date(timestamp_1.date())
                start_time_entry.set(timestamp_1.strftime("%H:%M"))


        # Assume current_date and current_time are the current values in the entries
        current_date = end_date_entry.get_date()
        current_time = end_time_entry.get()
        
        if match_end:
            timestamp_str_2 = match_end.group(0)
            timestamp_2 = datetime.strptime(timestamp_str_2, "%Y-%m-%dT%H:%M:%S")

            # Check if the current values exist
            if current_date and current_time:
                current_timestamp = datetime.strptime(end_time_entry.get(), "%H:%M")
                # Convert current date and time to datetime for comparison
                current_datetime = datetime.combine(current_date, current_timestamp.time())

                # Check if the new timestamp is less than the current one
                if timestamp_2 > current_datetime:
                    # Populate the start_date_entry
                    end_date_entry.set_date(timestamp_2.date())
                    end_time_entry.set(timestamp_2.strftime("%H:%M"))
            else:
                end_date_entry.set_date(timestamp_2.date())
                end_time_entry.set(timestamp_2.strftime("%H:%M"))


def select_directory():
    """
    select_directory(): Opens a directory dialog for the user to select a directory. 
    Updates the file_entry field with the selected directory's path.
    """
    initial_dir = file_entry.get()  # Get the current value in the entry (default or user-selected)
    directory_name = filedialog.askdirectory(initialdir=initial_dir)

    if directory_name:
        file_entry.config(state="normal")  # Change it back to normal (editable)
        file_entry.delete(0, tk.END)
        file_entry.insert(0, directory_name)
        # Make the file_entry field read-only
        file_entry.config(state="readonly")
        #html_label.set_html("")
        
        # Call the function to fill out the fields with default values
        fill_fields_with_default(directory_name)


def on_end_combobox_click(event):
    """
    Select the end_time_combobox with the next greater value from the current value

    Args:
        event (Tkinter.Event): The event triggered by the combobox click.
    """
    # Get the current selection
    current_value = end_time_entry.get()

    # Parse the current time
    current_hours, current_minutes = map(int, current_value.split(":"))

    # Find the next greater value or wrap around to the first value
    values = end_time_entry["values"]
    index = 0

    for i, value in enumerate(values):
        hours, minutes = map(int, value.split(":"))
        if (hours > current_hours) or (
            hours == current_hours and minutes > current_minutes
        ):
            index = i
            break

    # Set the current attribute to the index + 1 (next value)
    end_time_entry.current(index)


def on_start_combobox_click(event):
    """
    Updates the start time combobox with the next greater value.

    Args:
        event (Tkinter.Event): The event triggered by the combobox click.
    """
    # Get the current selection
    current_value = start_time_entry.get()

    # Parse the current time
    current_hours, current_minutes = map(int, current_value.split(":"))

    # Find the next greater value or wrap around to the first value
    values = start_time_entry["values"]
    index = 0

    for i, value in enumerate(values):
        hours, minutes = map(int, value.split(":"))
        if (hours > current_hours) or (
            hours == current_hours and minutes > current_minutes
        ):
            index = i
            break

    # Set the current attribute to the index + 1 (next value)
    start_time_entry.current(index)



def process_log(log_file, start, end):
    """
    Process a single log file and return the HTML representation.

    Args:
        log_file (str): Path to the log file.
        start (str): Beginning timestamp.
        end (str): End timestamp.

    Returns:
        str: HTML representation of the log file.
    """
    html_log = log_parser(log_file[1], beginning_timestamp=start, end_timestamp=end)
    filename = os.path.basename(log_file[0])
    return f"<h3>{filename}</h3>" + html_log

def process_logs_multithreaded(log_files_list, start, end):
    """
    Process multiple log files in parallel using multithreading.

    Args:
        log_files_list (list): List of log file paths.
        start (str): Beginning timestamp.
        end (str): End timestamp.

    Returns:
        str: Combined HTML representation of all log files.
    """
    html_text = ""

    # Using ThreadPoolExecutor for multithreading
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Process each log file concurrently
        futures = [executor.submit(process_log, log_file_pair, start, end) for log_file_pair in log_files_list]

        # Collect the results as they become available
        for future in concurrent.futures.as_completed(futures):
            html_log = future.result()
            html_text += html_log

    return html_text

def ok_action():
    """
    Validates user input, parses log file, and updates the HTML label.

    If a valid log file path is provided, extracts start and end timestamps, parses the log file
    within the specified time frame, and updates the HTML label with the parsed content. Displays
    an info message if the file path is invalid or empty.

    Note:

    Raises:
    - No specific exceptions are caught or raised.

    Returns:
    - None
    """
    logs_dir = file_entry.get()
    if logs_dir == "" or not os.path.isdir(logs_dir):
        messagebox.showinfo("Info", "Please select a new directory with mms log files")
    else:
        start = start_date_entry.get() + " " + start_time_entry.get()
        end = end_date_entry.get() + " " + end_time_entry.get()
        html_text = ""
        html_text = process_logs_multithreaded(log_files_list, start, end)
        open_web(html_text)
        delete_temporary_files(log_files_list)


def open_web(html_content):
    html_log = """ <html><body>""" + html_content + """ </body> </html> """
    # Create a temporary file
    temp = tempfile.NamedTemporaryFile(delete=False, suffix='.html')
    temp.write(html_log.encode('utf-8'))
    temp.close()

    # Open the file in the web browser
    webbrowser.open_new_tab('file://' + os.path.realpath(temp.name))

def cancel_action():
    """Cancels the action and closes the main Tkinter window."""
 
    root.destroy()


log_files_list = []
root = tk.Tk()

default_directory = os.getcwd()  # Get the current working directory

tk.Label(root, text="Log file location:").grid(row=0)
file_entry = tk.Entry(root,width=30)
file_entry.insert(0, default_directory)  # Set the default directory

# Make the file_entry field read-only
file_entry.config(state="readonly")
file_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=select_directory).grid(row=0, column=2)

tk.Label(root, text="Start Time frame:").grid(row=1)
start_date_entry = DateEntry(root)
start_date_entry.grid(row=1, column=1)
start_time_entry = ttk.Combobox(
    root, values=[f"{i:02d}:{j:02d}" for i in range(24) for j in range(0, 60, 15)]
)
start_time_entry.grid(row=1, column=2)

# Bind the click event to the §§
start_time_entry.bind("<Button-1>", on_start_combobox_click)


tk.Label(root, text="End Time frame:").grid(row=2)
end_date_entry = DateEntry(root)
end_date_entry.grid(row=2, column=1)
end_time_entry = ttk.Combobox(
    root, values=[f"{i:02d}:{j:02d}" for i in range(24) for j in range(0, 60, 15)]
)
end_time_entry.grid(row=2, column=2)
end_time_entry.bind("<Button-1>", on_end_combobox_click)


tk.Button(root, text="OK", command=ok_action).grid(row=3, column=0)
tk.Button(root, text="Cancel", command=cancel_action).grid(row=3, column=1)

root.mainloop()
