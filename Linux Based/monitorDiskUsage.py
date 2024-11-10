'''
Problem: 

Write a Python script that monitors the disk space usage of a Linux machine and sends 
an alert (e.g., an email or Slack message) if the usage exceeds a certain threshold.

Solution:
1. Use the subprocess module to call the df command and parse its output.
2. Compare disk usage against a threshold and send an alert if necessary.
3. Use a library like smtplib for sending email notifications or a library for integrating with Slack.

'''

import subprocess
import smtplib
from email.mime.text import MIMEText

def check_disk_usage(threshold=90):
    # Run the df command
    df_output = subprocess.check_output(['df', '/']).decode('utf-8')
    # Extract the percentage of disk usage
    usage_percentage = int(df_output.splitlines()[1].split()[4][:-1])

    if usage_percentage > threshold:
        send_alert(usage_percentage)

def send_alert(usage_percentage):
    msg = MIMEText(f"Disk usage has exceeded threshold. Current usage is {usage_percentage}%")
    msg['Subject'] = 'Disk Space Alert'
    msg['From'] = 'admin@anydomain.com'
    msg['To'] = 'me@anydomain.com'

    with smtplib.SMTP('smtp.mydomain.com') as server:
        server.login('my_email', 'my_password')
        server.sendmail(msg['From'], msg['To'], msg.as_string())

if __name__ == '__main__':
    check_disk_usage()