'''
Problem:
Write a Python script that deploys a service to a Linux system using systemd. 
The script should check if the service is running, and if not, it should start the service.

'''

import subprocess

SERVICE_NAME = 'my_service'

def check_service_status():
    try:
        status = subprocess.check_output(['systemctl', 'is-active', SERVICE_NAME]).decode('utf-8').strip()
        return status
    except subprocess.CalledProcessError:
        return 'inactive'

def start_service():
    subprocess.check_call(['systemctl', 'start', SERVICE_NAME])
    print(f"Service {SERVICE_NAME} started.")

def deploy_service():
    status = check_service_status()
    if status == 'inactive':
        print(f"Service {SERVICE_NAME} is not running. Starting it...")
        start_service()
    else:
        print(f"Service {SERVICE_NAME} is already running.")

if __name__ == '__main__':
    deploy_service()
