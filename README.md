# backup_grep

we are looking for the most popular backup errors in MMS0.log file 

**Installation:**
0. 
   ```
   brew install python3
   ```
1. Clone the repository:
   ```
   gh repo clone Vodyanoy17/backup_grep
   ```

1. create a virtual environment
   ```
   python3 -m venv <venv_name>
   source <venv_name>/bin/activate
   ```
2. install the packages according to the configuration file
   ```
   $ pip install -r requirements.txt
   ```
4. Example of execution
   ```
    <venv_name>/bin/python /backup_grep/grep/bckgrepgui.py
   ```




