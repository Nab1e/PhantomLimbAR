import numpy as np
import scipy.io
from ModelTraining import ModelTraining
from Features import calculateWavelength
from Features import zeroCrossingRate
from Features import calculateAbsMean

# Define x-axis values for the first 400 points
time_values = np.arange(1, 36001)

# Create the matrix for storing data
k = 12600
matrix = [np.zeros((k, 4)) for _ in range(10)]
mat_data = scipy.io.loadmat('1.mat')
my_struct = mat_data['recSession']
data = my_struct['tdata']
tdata = data[0, 0]


# Populate the matrix
for p in range(10):
    for i in range(4):
        c = 0
        k = 0

        # Plot the first 400 points of the specified column of recSession.tdata against time_values
        isDivisible = True
        for t in range(36000):
            c += 1
            if c % 6000 == 0:
                isDivisible = not isDivisible
                c = 0
            if isDivisible and c > 1800:
                matrix[p][k, i] = tdata[c, i, p]
                k += 1

segment_size = 400
num_segments = k // segment_size

# Initialize a list to store the results
result_matrix = [np.zeros((num_segments, 12)) for _ in range(10)]


# Process the data
for p in range(10):
    for segment in range(num_segments):
        for i in range(4):
            segment_data = matrix[p][(segment * segment_size):(segment + 1) * segment_size, i]
            result_matrix[p][segment, i] = calculateWavelength(segment_data)
            result_matrix[p][segment, i + 4] = zeroCrossingRate(segment_data)
            result_matrix[p][segment, i + 8] = calculateAbsMean(segment_data)

# Printing the result matrix for the first class (change the index if needed)
ModelTraining(result_matrix,4)