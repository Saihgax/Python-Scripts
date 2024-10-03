'''
TCP Server

A server listens via a listening socket for new connections, 
1. establishes them, 
2. gets the client's requests, and 
3. communicates the requested data in its response to the client.
'''

import socket

def tcp_server(host='0.0.0.0', port=8080):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Listen for incoming connections (max 5 clients per queue)
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept() # accept(): Accepts a connection from a client and returns a new socket for communication.
        try:
            print(f"Connection from the {client_address}")

            # Receive data from the client (1024 bytes at a time)
            data = client_socket.recv(1024)
            if data:
                print(f"Received message: {data.decode()}")
                # Send response back to the client
                response = "Hello, Client!"
                client_socket.sendall(response.encode())
            else:
                print("No data received from the client.")

        finally:
            # Clean up connection
            client_socket.close()

if __name__ == "__main__":
    tcp_server()