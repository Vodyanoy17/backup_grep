import re
import os
import tkinter as tk
from datetime import datetime
from grep_bck import log_parser
from tkhtmlview import HTMLLabel
from tkinter import ttk #, scrolledtext
from tkcalendar import DateEntry #, Calendar, 
from tkinter import filedialog, messagebox# #simpledialog, 

def fill_fields_with_default(log_file):
    """_summary_

    Args:
        log_file (_type_): _description_
    """
    with open(log_file, "rb") as file:
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
        match_start = re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", second_line )
        match_end = re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", last_line)
        if match_start:
            timestamp_str_1 = match_start.group(0)
            timestamp_1 = datetime.strptime(timestamp_str_1, "%Y-%m-%dT%H:%M:%S")

            # Populate the start_date_entry, start_time_entry, and other relevant fields with default values
            start_date_entry.set_date(timestamp_1.date())
            start_time_entry.set(timestamp_1.strftime("%H:%M"))

        if match_end:
            timestamp_str_2 = match_end.group(0)
            timestamp_2 = datetime.strptime(timestamp_str_2, "%Y-%m-%dT%H:%M:%S")

            # Populate the start_date_entry
            end_date_entry.set_date(timestamp_2.date())
            end_time_entry.set(timestamp_2.strftime("%H:%M"))
        

def select_file():
    """
    select_file(): Opens a file dialog for the user to select a file. 
    Updates the file_entry field with the selected file's path and fills out other 
    fields with default values based on the selected file.
    """
    initial_dir = (
        file_entry.get()
    )  # Get the current value in the entry (default or user-selected)
    filename = filedialog.askopenfilename(initialdir=initial_dir)

    if filename:
        file_entry.config(state="normal")  # Change it back to normal (editable)
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filename)
        # Make the file_entry field read-only
        file_entry.config(state="readonly")
        html_label.set_html("")
        

        # Call the function to fill out the fields with default values
        fill_fields_with_default(filename)


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
    log_file = file_entry.get()
    if log_file == "" or not os.path.isfile(log_file):
        messagebox.showinfo("Info", "Please select a file")
    else:
        start = start_date_entry.get() + " " + start_time_entry.get()
        end = end_date_entry.get() + " " + end_time_entry.get()
        html_log = log_parser(
            log_file, beginning_timestamp=start, end_timestamp=end
        )

        html_label.set_html(html_log)


def cancel_action():
    """Cancels the action and closes the main Tkinter window."""
    root.destroy()


root = tk.Tk()

default_directory = os.getcwd()  # Get the current working directory

tk.Label(root, text="Log file location:").grid(row=0)
file_entry = tk.Entry(root,width=30)
file_entry.insert(0, default_directory)  # Set the default directory

# Make the file_entry field read-only
file_entry.config(state="readonly")
file_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=select_file).grid(row=0, column=2)

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

# Horizontal separation line
separator = ttk.Separator(root, orient="horizontal")
separator.grid(row=4, column=0, columnspan=3, sticky="ew", pady=10)

# Adding an HTMLLabel below the existing code
html_label = HTMLLabel(root, html="")
html_label.grid(row=6, column=0, columnspan=3, pady=10, sticky="nsew")

# Configure grid column and row properties to make the HTMLLabel resize with the main window
root.columnconfigure(0, weight=1)
root.rowconfigure(6, weight=1)

root.mainloop()
