# backup_grep/backup_log_map

we are looking for the most popular backup errors in MMS0.log file 

**Installation:**

1. To install python on macOS
   ```
   brew install python3
   ```
2. Clone the repository:
   ```
   gh repo clone Vodyanoy17/backup_grep
   ```

3. create a virtual environment
   ```
   python3 -m venv venv1
   source venv1/bin/activate
   ```
4. install the packages according to the configuration file
   ```
   $ python3 -m pip install --upgrade pip
   $ pip install -r backup_grep/requirements.txt
   ```
   Solution for Linux, Windows (WSL/Ubuntu) and MacOS: Please install `python-tk` manually from Homebrew
   ```
   $ brew install python-tk
   ````
   
6. Example of execution grep ustility
   ```
    venv1/bin/python backup_grep/grep/bckgrepgui.py
   ```
<img width="705" alt="image" src="https://github.com/Vodyanoy17/backup_grep/assets/35487262/7868e60d-1295-4dcb-8bd1-fc656529a074">

7. Example of execution grep backup_log_map 
 ```
    venv1/bin/python  backup_grep/log_map/backup_log_map.py [mms0 log file]
   ```
<img width="775" alt="image" src="https://github.com/Vodyanoy17/backup_grep/assets/35487262/7d52a1d0-be6c-481f-afe5-32756c55fb1c">



