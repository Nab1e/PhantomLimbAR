import numpy as np
from scipy.signal import find_peaks
from GetFFT import GetFFT
def GetSigFeatures(data, sF, fID):

    # General information required to calculate different signal features
    # other processing is added by specific features in their functions
    procFeatures = {
        "ch": len(data[0, :]),
        "sp": len(data[:, 0]),
        "sF": sF,
        "data": data,
        "absdata": abs(data),
        "f": {},
    }

    # Add data of the fast Fourier transform if a frequency feature is required
    # This verification needs to be optimized
    for i in range(len(fID)):
        temp = fID[i]
        if temp[0] == 'f':
            procFeatures = GetFFT(procFeatures)
            break

    # Calculate signal features
    for i in range(len(fID)):
        fName = 'GetSigFeatures_' + fID[i]
        procFeatures = eval(fName)(procFeatures)

    xFeatures = procFeatures["f"]

    return xFeatures
def GetSigFeatures_tmn(pF):
    # 2011-07-27 Max Ortiz / Creation
    pF["f"]["tmn"]=0
    DataMatrix = []

    for i in range(4):
        dt = [row[i] for row in pF["data"]]
        dt = np.array(dt)
        DataMatrix.append(dt.mean())
        pF["f"]["tmn"] = DataMatrix
    return pF

def GetSigFeatures_tmabs(pF):
    # 2011-07-27 Max Ortiz / Creation
    pF["f"]["tmabs"]=0
    DataMatrix = []

    for i in range(4):
        dt = [row[i] for row in pF["absdata"]]
        dt = np.array(dt)
        DataMatrix.append(dt.mean())
        pF["f"]["tmabs"] = DataMatrix
    return pF

def calculate_wavelength(data):
    # Calculate the wavelength of a numeric array 'data'
    
    # Initialize variables
    zero_crossings = []
    
    # Detect zero-crossings
    for i in range(1, len(data)):
        if (data[i] * data[i-1]) < 0:
            zero_crossings.append(i)
    
    # Calculate the wavelength as the difference between consecutive zero-crossings
    wavelengths = np.diff(zero_crossings)
    
    # Calculate the mean wavelength
    wavelength = np.mean(wavelengths)
    
    return wavelength


def GetSigFeatures_twl(pF):
    # Waveform Length (acumulative changes in the length)
    # 2011-07-27 Max Ortiz / Creation
    #mdata = np.vstack((np.zeros(pF["ch"]), pF["data"][:-1, :]))
    #pF["f"]["twl"] = np.sum(np.abs(pF["data"] - mdata))
    DataMatrix = []
    
    for j in range(4):
        c=0
        dt = [row[j] for row in pF["data"]]
        wl = calculate_wavelength(dt)
        DataMatrix.append(wl)
        pF["f"]["twl"] = DataMatrix

    return pF



def GetSigFeatures_tzc(pF):
    # 2011-07-27 Max Ortiz / Creation
    # Check if tmabs is available
    #if "tmabs" not in pF["f"]:
    #    pF = GetSigFeatures_tmabs(pF)
    #pF["f"]["tzc"] = np.array([])
    #tmp = np.tile(1, (pF["sp"], 1))
    DataMatrix = []
    for i in range(4):
       dt = [row[i] for row in pF["data"]]
       dt = np.array(dt)
       threshold = np.mean(np.abs(dt))
    
    # Count the number of times the signal crosses the threshold
       zero_crossings = np.where(np.diff(np.sign(dt - threshold)))[0]
    
    # Calculate the zero-crossing rate
       zero_crossing_rate = len(zero_crossings) / (len(dt) - 1)

       DataMatrix.append(zero_crossing_rate)
    pF["f"]["tzc"] =  DataMatrix 


    return pF
 
#sample_data = np.random.rand(100, 5)  # 100 samples and 5 channels

# Sample values for sF, fFilter, and fID
#sample_sF = 1000  # Replace with your actual sampling frequency
#sample_fFilter = None  # You can specify a filter if needed
#sample_fID = ["tmn", "tvar", "twl", "trms", "tzc"]  # Replace with your desired feature IDs

# Call the GetSigFeatures function
#xFeatures = GetSigFeatures(sample_data, sample_sF, sample_fID)

# Print the resulting feature dictionary
