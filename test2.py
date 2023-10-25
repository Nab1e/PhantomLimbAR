import socket

server_host = '127.0.0.1'  # Replace with the server's IP address or hostname
server_port = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))

# Receive data from the server
while True:
    data = client_socket.recv(1024)
    print(data)
    if not data:
        break  # Connection closed by the server
    data_str = data.decode('utf-8')  # Convert bytes to a string assuming UTF-8 encoding
    print(data_str)

    print("dtt")
    data = [float(x) for x in data_str.split(',')]
    print(data)

# Close the client socket when done
client_socket.close()
