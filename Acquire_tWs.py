import numpy as np

def Acquire_tWs(client_socket, nCh, tWs):
    
    cData = np.zeros((tWs, nCh), dtype=float)  # Initialize the data structure that the function must return

    for sampleNr in range(tWs):
        
        data = client_socket.recv(1024)
        data_str = data.decode('utf-8')  # Convert bytes to a string assuming UTF-8 encoding
        data = [float(x) for x in data_str.split(',')]
        cData[sampleNr, :] = data
    
    return cData

