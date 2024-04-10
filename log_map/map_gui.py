import tkinter as tk
from tkinter import filedialog
from log_map.file_sort import concat_all_files
import backup_log_map 

file_array = []
def select_files():

    global file_array
    # Open the file dialog with the option to select multiple files
    file_paths = filedialog.askopenfilenames(title="Select files")

    # Convert the tuple of file paths to a list
    file_array = list(file_paths)

    # Clear the listbox
    listbox.delete(0, tk.END)

    # Add the selected files to the listbox
    for file_path in file_array:
        listbox.insert(tk.END, file_path)
    return file_array


def run_function(file_array):
    #global file_array
    # Replace this with the function you want to run
    print("Running function with the following files:")
    output_file = concat_all_files(file_array)

    backup_log_map.log_scaner(output_file)

# Create the main window
root = tk.Tk()

# Create a frame for the listbox and scrollbars
frame = tk.Frame(root)
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a vertical scrollbar
vscrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a horizontal scrollbar
hscrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Create a listbox
listbox = tk.Listbox(frame, yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configure the scrollbars to scroll the listbox
vscrollbar.config(command=listbox.yview)
hscrollbar.config(command=listbox.xview)

# Create a button that will call the select_files function when clicked
select_button = tk.Button(root, text="Select Files", command=lambda: run_function(select_files()))
select_button.pack()

# Create a button that will exit the application when clicked
cancel_button = tk.Button(root, text="Exit", command=root.destroy)
cancel_button.pack()

# Start the main loop
root.mainloop()
