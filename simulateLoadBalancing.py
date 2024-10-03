'''
You are given a list of servers and each server 
has a server_id and a capacity (the maximum number of requests 
it can handle). Write a function to distribute a list of 
incoming requests to the servers in a round-robin fashion. 

If a server's capacity is full, the next server should 
handle the request.
'''

def distribute_requests(servers, requests):
    assigned_requests = {server['server_id']: [] for server in servers}
    capacities = {server['server_id']: server['capacity'] for server in servers}
    print(capacities)

    i = 0 
    for req in requests:
        while capacities[servers[i]]

servers = [
    {"server_id": "s1", "capacity": 2},
    {"server_id": "s2", "capacity": 3},
    {"server_id": "s3", "capacity": 1}
]

requests = ["req1", "req2", "req3", "req4", "req5", "req6"]

result = distribute_requests(servers, requests)
print(result)