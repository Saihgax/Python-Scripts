import re
from collections import defaultdict

def parse_log(lines):
    url_pattern = r'\"[A-Z]+\s(\S+)\sHTTP\/[0-9\.]+\"'
    unique_urls = set()

    for line in lines:
        match = re.search(url_pattern, line)
        if match:
            unique_urls.add(match.group(1))
    return unique_urls

def get_response_time(lines):
    url_pattern = r'\"([A-Z]+)\s\S+\sHTTP\/[\d\.]+\"\s\d+\s(\d+)ms'
    method_times = defaultdict(list)

    for line in lines:
        match = re.search(url_pattern, line)
        if match:
            method, response_time = match.groups()
            method_times[method].append(int(response_time))
    avg_times = {method: sum(times)/len(times) for method, times in method_times.items()}
    return avg_times


with open('sample.log', 'r') as logfile:
    lines = logfile.readlines()
    print(parse_log(lines))
    print(get_response_time(lines))