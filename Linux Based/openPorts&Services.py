'''
Problem: Write a Python script to check for open ports on a Linux server and list the services running on those ports.

Solution:

1. Use netstat or ss to get open ports.
2. Use ps to correlate the ports to specific running services.

'''

import subprocess

def get_open_ports():
    # Get open ports using ss
    ss_output = subprocess.check_output(['ss', '-tuln']).decode('utf-8')
    open_ports = []
    for line in ss_output.splitlines()[1:]:
        columns = line.split()
        open_ports.append(columns[4].split(':')[-1])
    return open_ports

def get_service_by_port(port):
    # Find service running on the given port using ps
    ps_output = subprocess.check_output(['ps', '-aux']).decode('utf-8')
    for line in ps_output.splitlines():
        if f":{port}" in line:
            return line
    return None

def check_services():
    open_ports = get_open_ports()
    for port in open_ports:
        service = get_service_by_port(port)
        if service:
            print(f"Port {port} is open, running service: {service}")
        else:
            print(f"Port {port} is open, but no service found.")

if __name__ == '__main__':
    check_services()
