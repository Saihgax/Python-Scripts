'''
Problem:

Write a Python script that checks the size of a log file (e.g., /var/log/syslog) 
and rotates it if the file size exceeds a threshold (e.g., 100MB). 
The script should create a backup and compress the old log file.

Solution:

Check the size of the log file.
If it exceeds the threshold, rotate the log by renaming it and compressing the old file.
Create a new empty log file.


'''
import os, gzip, shutil, time

LOG_FILE = "/var/log/syslog"
BACKUP_DIR = "/var/log/backup"

def rotate_log():
    if os.path.getsize(LOG_FILE) > 100 * 1024 * 1024:
        timestamp = time.strftime("%Y%m%d%H%M%S")
        backup_log = os.path.join(BACKUP_DIR, f"syslog.{timestamp}.gz")
        with open(LOG_FILE, 'rb') as f_in:
            with gzip.open(backup_log, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        # Clear the original log file
        with open(LOG_FILE, 'w') as f:
            f.truncate(0)

        print(f"Log rotated and saved to {backup_log}")
    else:
        print("Log file size is under the threshold.")

if __name__ == '__main__':
    rotate_log()
