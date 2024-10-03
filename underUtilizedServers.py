
'''
You are given a list of servers where each server has 
server_id, requests_handled, and response_time. 
Write a function to identify underutilized servers based 
on a threshold for requests handled and response time.
'''

def find_underutilized_servers(servers, req_threshold, resp_threshold):
    underutilized = []
    for server in servers:
        if server['requests_handled'] < req_threshold and server['response_time'] < resp_threshold:
            underutilized.append(server)
    return underutilized


servers = [
    {"server_id": "s1", "requests_handled": 100, "response_time": 120},
    {"server_id": "s2", "requests_handled": 50, "response_time": 80},
    {"server_id": "s3", "requests_handled": 200, "response_time": 150}
]

result = find_underutilized_servers(servers, 150, 100)
print(f"Underutilized Servers: {result}")