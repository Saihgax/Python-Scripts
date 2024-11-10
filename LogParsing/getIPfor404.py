
import re

# Sample log file line format: '127.0.0.1 - - [12/Nov/2024:10:10:10 +0000] "GET /page HTTP/1.1" 404 1234'
log_file = 'server.log'

def extract404(log_file):
    ip_pattern = r'(\d+\.\d+\.\d+\.\d+).*\s404\s'
    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(ip_pattern, line)
            if match:
                print(match.group(1))

extract404(log_file)