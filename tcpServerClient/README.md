## How To Run

1. Start the server
    - Run the **tcp_server.py** script. The server will start listening on port 8080.
    - Example command: python tcp_client.py

2. Start the client
    - Run the **tcp_client.py** script to connect to the server, send the message, and receive the server's response.
    - Example command: python tcp_client.py


## Expected Output

- Server

    ```python
    Server listening on 0.0.0.0:8080
    Connection from ('127.0.0.1', 12345)
    Received message: Hello, Server!
    ```

- Client

    ```python
    Received from server: Hello, Client!
    ```
    