from datetime import datetime
from grep_bck import log_parser
from tkcalendar import Calendar, DateEntry
from tkinter import filedialog, simpledialog, messagebox
from tkinter import ttk
import os
import re
import tkinter as tk

def fill_fields_with_default(log_file):
    with open(log_file, 'r') as file:
        # skip the first line
        _ = file.readline()

        # Read the second line again to get the actual second line
        second_line = file.readline()
        # Use regular expression to find the timestamp
        match = re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', second_line)
        if match:
            timestamp_str = match.group(0)
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S')

            print(timestamp_str)
            # Populate the start_date_entry, start_time_entry, and other relevant fields with default values
            start_date_entry.set_date(timestamp.date())
            start_time_entry.set(timestamp.strftime('%H:%M'))

            # Populate the start_date_entry
            end_date_entry.set_date(timestamp.date())
            end_time_entry.set(timestamp.strftime('%H:%M'))

def select_file():
    initial_dir = file_entry.get()  # Get the current value in the entry (default or user-selected)
    filename = filedialog.askopenfilename(initialdir=initial_dir)

    if filename:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filename)

        # Call the function to fill out the fields with default values
        fill_fields_with_default(filename)

# ...


def ok_action():
    log_file = file_entry.get()
    if log_file == "" or not os.path.isfile(log_file):
        messagebox.showinfo("Info", "Please select a file")
    else:
        start = start_date_entry.get() + " " + start_time_entry.get()
        end = end_date_entry.get() + " " + end_time_entry.get()
        log_parser(log_file, beginning_timestamp=start, end_timestamp=end )

def cancel_action():
    root.destroy()

root = tk.Tk()

default_directory = os.getcwd()  # Get the current working directory

tk.Label(root, text="Log file location:").grid(row=0)
file_entry = tk.Entry(root)
file_entry.insert(0, default_directory)  # Set the default directory
file_entry.grid(row=0, column=1)
tk.Button(root, text='Browse', command=select_file).grid(row=0, column=2)

tk.Label(root, text="Start Time frame:").grid(row=1)
start_date_entry = DateEntry(root)
start_date_entry.grid(row=1, column=1)
start_time_entry = ttk.Combobox(root, values=[f"{i:02d}:{j:02d}" for i in range(24) for j in range(0, 60, 15)])
start_time_entry.grid(row=1, column=2)

tk.Label(root, text="End Time frame:").grid(row=2)
end_date_entry = DateEntry(root)
end_date_entry.grid(row=2, column=1)
end_time_entry = ttk.Combobox(root, values=[f"{i:02d}:{j:02d}" for i in range(24) for j in range(0, 60, 15)])
end_time_entry.grid(row=2, column=2)

tk.Button(root, text='OK', command=ok_action).grid(row=3, column=0)
tk.Button(root, text='Cancel', command=cancel_action).grid(row=3, column=1)

root.mainloop()
