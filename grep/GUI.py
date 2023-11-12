from datetime import datetime
from grep_bck import log_parser
from tkcalendar import Calendar, DateEntry
from tkinter import filedialog, simpledialog, messagebox
from tkinter import ttk
import os
import re
from tkinter import ttk, scrolledtext
import tkinter as tk
from tkinter import Tk, Text, Scrollbar, Frame, Label, Button
#from colorama import Fore, Back, init


def fill_fields_with_default(log_file):
    with open(log_file, "r") as file:
        # skip the first line
        _ = file.readline()

        # Read the second line again to get the actual second line
        second_line = file.readline()
        # Use regular expression to find the timestamp
        match = re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", second_line)
        if match:
            timestamp_str = match.group(0)
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S")

            # Populate the start_date_entry, start_time_entry, and other relevant fields with default values
            start_date_entry.set_date(timestamp.date())
            start_time_entry.set(timestamp.strftime("%H:%M"))

            # Populate the start_date_entry
            end_date_entry.set_date(timestamp.date())
            end_time_entry.set(timestamp.strftime("%H:%M"))


def select_file():
    initial_dir = (
        file_entry.get()
    )  # Get the current value in the entry (default or user-selected)
    filename = filedialog.askopenfilename(initialdir=initial_dir)

    if filename:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filename)

        # Call the function to fill out the fields with default values
        fill_fields_with_default(filename)


def on_end_combobox_click(event):
   # Get the current selection
    current_value = end_time_entry.get()

    # Parse the current time
    current_hours, current_minutes = map(int, current_value.split(':'))

    # Find the next greater value or wrap around to the first value
    values = end_time_entry['values']
    index = 0

    for i, value in enumerate(values):
        hours, minutes = map(int, value.split(':'))
        if (hours > current_hours) or (hours == current_hours and minutes > current_minutes):
            index = i
            break

    
    # Set the current attribute to the index + 1 (next value)
    end_time_entry.current(index)

def on_start_combobox_click(event):
    # Get the current selection
    current_value = start_time_entry.get()

    # Parse the current time
    current_hours, current_minutes = map(int, current_value.split(':'))

    # Find the next greater value or wrap around to the first value
    values = start_time_entry['values']
    index = 0

    for i, value in enumerate(values):
        hours, minutes = map(int, value.split(':'))
        if (hours > current_hours) or (hours == current_hours and minutes > current_minutes):
            index = i
            break

    
    # Set the current attribute to the index + 1 (next value)
    start_time_entry.current(index)



def ok_action():
    log_file = file_entry.get()
    if log_file == "" or not os.path.isfile(log_file):
        messagebox.showinfo("Info", "Please select a file")
    else:
        start = start_date_entry.get() + " " + start_time_entry.get()
        end = end_date_entry.get() + " " + end_time_entry.get()
        log_result = log_parser(log_file, beginning_timestamp=start, end_timestamp=end)

        test_text_colorful = f"{log_result}"  # 31 corresponds to red color in ANSI escape codes
        text_widget.insert(tk.END, test_text_colorful + "\n")

def cancel_action():
    root.destroy()


root = tk.Tk()

default_directory = os.getcwd()  # Get the current working directory

tk.Label(root, text="Log file location:").grid(row=0)
file_entry = tk.Entry(root)
file_entry.insert(0, default_directory)  # Set the default directory
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
start_time_entry.bind('<Button-1>', on_start_combobox_click)


tk.Label(root, text="End Time frame:").grid(row=2)
end_date_entry = DateEntry(root)
end_date_entry.grid(row=2, column=1)
end_time_entry = ttk.Combobox(
    root, values=[f"{i:02d}:{j:02d}" for i in range(24) for j in range(0, 60, 15)]
)
end_time_entry.grid(row=2, column=2)
end_time_entry.bind('<Button-1>', on_end_combobox_click)


tk.Button(root, text="OK", command=ok_action).grid(row=3, column=0)
tk.Button(root, text="Cancel", command=cancel_action).grid(row=3, column=1)

# Horizontal separation line
separator = ttk.Separator(root, orient="horizontal")
separator.grid(row=4, column=0, columnspan=3, sticky="ew", pady=10)

text_frame = tk.Frame(root)
text_frame.grid(row=5, column=0, columnspan=3, pady=10, sticky="nsew")

# Create the text_widget first
text_widget = scrolledtext.ScrolledText(
    text_frame, height=10, wrap=tk.NONE
)
text_widget.pack(expand=True, fill="both")

# Then, add a horizontal scroll bar to the text widget
scrollbar = ttk.Scrollbar(text_frame, orient="horizontal", command=text_widget.xview)
scrollbar.pack(side="bottom", fill="x")

text_widget.configure(xscrollcommand=scrollbar.set)  # Configure xscrollcommand after widget creation
# Configure tags for formatting
text_widget.tag_configure("bold", font=("TkDefaultFont", 12, "bold"))



# Configure grid column and row properties to make the text widget resize with the main window
root.columnconfigure(0, weight=1)
root.rowconfigure(5, weight=1)

root.mainloop()
