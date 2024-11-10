'''
You have a time series of memory usage data from a server. 
Write a function to detect whether memory usage increases 
continuously for more than 3 consecutive periods 
(indicating a potential memory leak).
'''

def detect_memory_leak(logs):
    count = 0
    for i in range(1, len(logs)):
        prev = logs[i-1]
        curr = logs[i]

        if prev["memory_usage"] < curr["memory_usage"]:
            count += 1
        else:
            count = 0
    
    if count >=3:
        return True
    return False

logs = [
    {"timestamp": "2023-09-01 00:00:00", "memory_usage": 400},
    {"timestamp": "2023-09-01 01:00:00", "memory_usage": 410},
    {"timestamp": "2023-09-01 02:00:00", "memory_usage": 420},
    {"timestamp": "2023-09-01 03:00:00", "memory_usage": 425},
]

result = detect_memory_leak(logs)
print(f"Memory Leak Detected: {result}")

