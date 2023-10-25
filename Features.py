
import numpy as np 

def calculateAbsMean(arr):
    # Calculate the absolute mean
    absMean = np.mean(np.abs(arr))
    return absMean
def zeroCrossingRate(data):
    # Calculate the zero-crossing rate of a numeric vector 'data'
    
    # Initialize the count of zero-crossings
    zcr = 0
    
    # Iterate through the data to count zero-crossings
    for i in range(1, len(data)):
        if data[i] * data[i - 1] < 0:
            zcr += 1
    
    # Calculate the zero-crossing rate as the count divided by (N - 1)
    zcr /= (len(data) - 1)
    
    return zcr
def calculateWavelength(data):
    # Calculate the wavelength of a numeric vector 'data'
    
    # Initialize variables
    zeroCrossings = []
    
    # Detect zero-crossings
    for i in range(1, len(data)):
        if data[i] * data[i - 1] < 0:
            zeroCrossings.append(i)
    
    # Calculate the wavelength as the difference between consecutive zero-crossings
    wavelengths = np.diff(zeroCrossings)
    
    # Calculate the mean wavelength
    wavelength = np.mean(wavelengths)
    
    return wavelength
