'''
Problem: 

Write a Python script that finds and kills zombie processes (processes with a status of Z) on a Linux machine.

Solution:

1. Use ps aux or ps -ef to get a list of processes.
2. Filter for processes with the status Z (zombie).
3. Use os.kill or subprocess to terminate the zombie processes.

'''

import subprocess, os, signal

def find_zombie_processes():
    ps_output = subprocess.check_output(['ps', 'aux']).decode('utf-8')

    zombie_processes = []
    for line in ps_output.splitlines()[1:]:
        columns = line.split()
        pid = columns[1]
        status = columns[7]

        if status == 'Z':
            zombie_processes.append(pid)

    return zombie_processes

def kill_process(pid):
    try:
        os.kill(int(pid), signal.SIGKILL)
        print(f"Killed zombie process with PID {pid}")
    except Exception as e:
        print(f"Error killing the process {pid}: {e}")

    if __name__ == '__main__':
        zombies = find_zombie_processes()
        if zombies:
            for pid in zombies:
                kill_process(pid)
        else:
            print("No zombie processes found.")
            

