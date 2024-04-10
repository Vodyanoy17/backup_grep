import os
import gzip
import heapq

def merge_sorted_files(file_list, output_file):
    # Open all files in read mode.
    files = [open(file, 'r') for file in file_list]

    # Use a heap to keep track of the smallest element in each file.
    heap = [(f.readline().strip(), i) for i, f in enumerate(files)]
    heapq.heapify(heap)

    # Open the output file in write mode.
    with open(output_file, 'w') as out_file:
        while heap:
            # Pop the smallest element from the heap and write it to the output file.
            smallest_entry, file_index = heapq.heappop(heap)
            out_file.write(smallest_entry + '\n')

            # Read the next line from the file that contained the smallest element.
            next_line = files[file_index].readline().strip()
            if next_line:
                # If the file is not empty, add the next line to the heap.
                heapq.heappush(heap, (next_line, file_index))

    # Close all input files.
    for f in files:
        f.close()

def get_all_unzip_log_files(file_array):
  """
  This function scans a directory for log files, sorts them by modification date in descending order,
  unzips gzip compressed files, and concatenates their content into a single output file.

  Args:
      directory (str): Path to the directory containing log files.

  Returns:
      str: Path to the concatenated output file (mms0.log.concat), or None if no files found.
  """

  # Initialize empty list to store file paths
  log_files = []

  # Iterate through files array  and fetch only mms0 files
  for filename in file_array:
    base_name = os.path.basename(filename)
        
    # Check if the file name starts with "mms0" and ends with ".log" or ".log.gz"
    if base_name.startswith("mms0") and (base_name.endswith(".log") or base_name.endswith(".log.gz")):
        print(f"{base_name} matches the criteria")

        # Handle gzipped files
        if filename.endswith(".gz"):
            unzip_filename = filename + ".log"
            with open(unzip_filename, "a") as outfile:
                with gzip.open(filename, "rb") as infile:
                    outfile.write(infile.read().decode())  # Decode for text processing
                    log_files.append(unzip_filename)
        else:
            log_files.append(filename)

  # Check if any files were found
  if not log_files:
    print("No log files found in the directory.")
    return None

  return log_files

def concat_all_files(file_array):
    file_list = get_all_unzip_log_files(file_array)
    output_file = 'concat_output.txt'
    merge_sorted_files(file_list, output_file)
    return output_file