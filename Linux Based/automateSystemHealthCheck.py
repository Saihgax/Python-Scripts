'''
Problem: Write a Python script that performs a 
1. basic system health check, 
2. reporting on CPU load, 
3. memory usage, disk usage, and running services. 

This could be used as part of a larger monitoring framework.


Solution:

1. Use subprocess to gather system metrics
2. Format the output and report on the health status
3. You can make it extensible by adding more system checks

'''

import subprocess
import json

def get_cpu_load():
    load = subprocess.check_output(['uptime']).decode('utf-8')
    return load.split("average:")[1].strip()

def get_memory_usage():
    memory = subprocess.check_output(['free', '-h']).decode('utf-8')
    return memory.splitlines()[1]

def get_disk_usage():
    disk = subprocess.check_output(['df', '-h']).decode('utf-8')
    return disk.splitlines()[1]

def get_running_services():
    services = subprocess.check_output(['ps', '-ef']).decode('utf-8')
    return services

def perform_health_check():
    health_report = {
        "cpu_load": get_cpu_load(),
        "memory_usage": get_memory_usage(),
        "disk_usage": get_disk_usage(),
        "running_services": get_running_services(),
    }
    return health_report

def main():
    health_report = perform_health_check()
    print(json.dumps(health_report, indent=4))

if __name__ == '__main__':
    main()