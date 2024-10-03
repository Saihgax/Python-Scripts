
'''
Given a list of dictionaries where each dictionary 
contains a timestamp, service, and latency (in milliseconds), 
write a function to identify services 
that exceed a latency threshold and report them.
'''

def find_latency_bottlenecks(logs, threshold):
    res = []
    for log in logs:
        if log["latency"] >= threshold:
            res.append(log)
    return res

logs = [
    {"timestamp": "2023-09-01 00:00:00", "service": "auth", "latency": 150},
    {"timestamp": "2023-09-01 01:00:00", "service": "database", "latency": 250},
    {"timestamp": "2023-09-01 02:00:00", "service": "cache", "latency": 100}
]

threshold = 200
result = find_latency_bottlenecks(logs, threshold)
print(f"Bottleneck Services: {result}")
