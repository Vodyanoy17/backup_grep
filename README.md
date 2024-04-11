# backup_grep/backup_log_map

## we are looking for the most popular  errors in MMS0.log file based on list of the errors

### Tested on `MAC M1` and `Windows10 64 x86`

**Installation:**

1. To install python on macOS
   ```
   $brew install python3
   ```
2. Clone the repository:
   ```
   MAC:
   $gh repo clone Vodyanoy17/backup_grep
   ```
   ```
   WINDOWS:
   >git clone https://github.com/Vodyanoy17/backup_grep.git .
   ```
3. create a virtual environment
   ```
   MAC:
   $ python3 -m venv venv1
   $ source venv1/bin/activate
   ```
   ```
   WINDOWS:
   > python -m venv venv1
   > venv1\Scripts\activate.bat
   ```
4. install the packages according to the configuration file
   ```
   MAC:
   $ python3 -m pip install --upgrade pip
   $ pip install -r backup_grep/requirements.txt
   ```
   ```
   WINDOWS:
   > python.exe -m pip install --upgrade pip
   > pip install -r requirements.txt
   ```
   Solution for Linux, Windows (WSL/Ubuntu) and MacOS: Please install `python-tk` manually from Homebrew
   ```
   $ brew install python-tk
   ```
   
6. Example of execution grep ustility
   ```
   MAC:
    venv1/bin/python backup_grep/grep/bckgrepgui.py
   ```
   ```
   WINDOWS
   >python grep\bckgrepgui.py
   ```
![image](https://github.com/Vodyanoy17/backup_grep/assets/35487262/46ab2c96-1a59-4aa9-8490-4e1c7d09a87a)

   
<img width="705" alt="image" src="https://github.com/Vodyanoy17/backup_grep/assets/35487262/7868e60d-1295-4dcb-8bd1-fc656529a074">

7. Example of execution grep backup_log_map from cli
   if you want to run it over several OM's logs you need to manually combine all files by `cat file1 file2 | sort > sorted.log`
   The GUI version with a more efficient method of sorting.
 ```
    venv1/bin/python  backup_grep/log_map/backup_log_map.py [mms0 logs directory]
   ```
<img width="775" alt="image" src="https://github.com/Vodyanoy17/backup_grep/assets/35487262/7d52a1d0-be6c-481f-afe5-32756c55fb1c">

8. The is an option to run GUI and select different files from several OM instances.
   ```/python /backup_grep/log_map/map_gui.py```
   <img width="692" alt="image" src="https://github.com/Vodyanoy17/backup_grep/assets/35487262/5e603a43-d150-431a-aa00-8ca0d2fe527f">


