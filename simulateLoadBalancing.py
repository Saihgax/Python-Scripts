'''
You are given a list of servers and each server 
has a server_id and a capacity (the maximum number of requests 
it can handle). Write a function to distribute a list of 
incoming requests to the servers in a round-robin fashion. 

If a server's capacity is full, the next server should 
handle the request.
'''
def distribute_requests(servers, requests):
    # Create a dictionary to store the assigned requests for each server
    assigned_requests = {server['server_id']: [] for server in servers}
    
    # Create a dictionary to track the remaining capacity of each server
    capacities = {server['server_id']: server['capacity'] for server in servers}
    
    i = 0  # Index to iterate through the servers in a round-robin manner
    
    for req in requests:
        # Find the next server with available capacity
        while capacities[servers[i]['server_id']] == 0:
            i = (i + 1) % len(servers)
        
        # Assign the request to the current server
        server_id = servers[i]['server_id']
        assigned_requests[server_id].append(req)
        
        # Decrease the capacity of the server
        capacities[server_id] -= 1
        
        # Move to the next server in a round-robin fashion
        i = (i + 1) % len(servers)
    
    return assigned_requests

# Example servers and requests
servers = [
    {"server_id": "s1", "capacity": 2},
    {"server_id": "s2", "capacity": 3},
    {"server_id": "s3", "capacity": 1}
]

requests = ["req1", "req2", "req3", "req4", "req5", "req6"]

# Call the function and print the result
result = distribute_requests(servers, requests)
print(result)
