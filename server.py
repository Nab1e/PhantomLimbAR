import socket
import time
import scipy.io
import numpy as np
host = '127.0.0.1'
port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)  # 1 is the maximum number of queued connections

print(f"Server is listening on {host}:{port}")

while True:
    try:
        # Accept a connection from a client
        mat_data = scipy.io.loadmat('1.mat')
        my_struct = mat_data['recSession']
        data = my_struct['tdata']
        data = data[0, 0]

        ch1 = data[:, 0, :]
        ch2 = data[:, 1, :]
        ch3 = data[:, 2, :]
        ch4 = data[:, 3, :]
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        # Access variables from the .mat file
        
        # Format the data and send it to the receiver
        for i in range(ch1.shape[1]):
            for j in range(ch1.shape[0]):
                j=j+1900
                message = f" {ch1[j][8]},{ch2[j][8]},{ch3[j][8]},{ch4[j][8]} "
                client_socket.send(message.encode())

                time.sleep(0.02)  # Optional delay to control the transmission rate

        # Close the client socket
        client_socket.close()

    except KeyboardInterrupt:
        break
