'''
TCP Client

Client creates a socket using the IP address and port of the server it wishes to connect to, 
1. initiates a connection, 
2. communicates its request to the server, and 
3. receives data in response. 

'''

import socket

def tcp_client(server_host='localhost', server_port=8080):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((server_host, server_port))
    
    try:
        # Send a message to the server
        message = "Hello, Server!"
        client_socket.sendall(message.encode())
        
        # Receive the server's response
        response = client_socket.recv(1024)
        print(f"Received from server: {response.decode()}")
    
    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    tcp_client()
