import numpy as np
import time
import socket
from OneShotRealtimePatRec import OneShotRealtimePatRec
from Acquire_tWs import Acquire_tWs
import scipy.io

patRecX = scipy.io.loadmat('nabill.mat')
patRecX = patRecX['patRec']


    # Clear global and persistent variables
global patRec, handles, nTW, procT, tempData, outVectorMotorLast, thresholdGUIData
patRec = patRecX
nTW = 1
procT = []
tempData = []

outVectorMotorLast = np.zeros(patRec['nOuts'][0][0][0][0])

    # Get needed info from patRec structure
sF = patRec['sF'][0][0][0][0]
nCh = 4

    # Get sampling time
sT = 100000
tW = 0.2  # Time window size
tWs = 400  # Time window samples

cData = np.zeros((tWs, nCh))




 # Define the server's host and port
server_host = '127.0.0.1'  # Replace with the server's IP address or hostname
server_port = 12345

    # Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
client_socket.connect((server_host, server_port))

deviceName = 'Arduino4Ch'
    # Magic time
    
def RealtimePatRec_OneShot(src, event):
    global patRec, nTW, procT, handles, tempData, outVectorMotorLast
    num_columns = event['Data'].shape[1]
    tempData = np.zeros((0, num_columns), dtype=float)  # Initialize an empty array with the same number of columns
    # ...

    # Now you can stack the arrays vertically
    tempData = np.vstack((tempData, event['Data']))
    # Keep saving all recorded data

    end_index = tempData.shape[0] - tWs

    tData = tempData[end_index:, :]


    # Only consider the data once it has at least the size of the time window

    if tData.shape[0] >= tWs-1:
        # Start of processing time
        procTimeS = time.time()

        # General routine for RealtimePatRec
        outMov, outVector, patRec = OneShotRealtimePatRec(tData, patRec)
        

        #print(outMov)
        # Next cycle
        nTW = nTW + 1
        
        # Finish of processing time
        procT.append(time.time() - procTimeS)


for timeWindowNr in range(20):
    cData= Acquire_tWs(client_socket, nCh, tWs)
    acquireEvent = {'Data': cData}
    RealtimePatRec_OneShot(0, acquireEvent)

    # Stop acquisition (we will need to make a condition to stop)
client_socket.close()



