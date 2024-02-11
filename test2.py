import socket

server_host = '127.0.0.1'  # Replace with the server's IP address or hostname
server_port = 25001
# Create a socket object

# Receive data from the server
for i in range(20000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((server_host, server_port))

    data = client_socket.recv(1024)
    data_str = data.decode('utf-8')  # Convert bytes to a string assuming UTF-8 encoding
    if(data_str):
        print(data_str)

