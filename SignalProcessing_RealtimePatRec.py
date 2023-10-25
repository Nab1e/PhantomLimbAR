import numpy as np
from GetSigFeatures import GetSigFeatures
from ApplyFeatureReduction import ApplyFeatureReduction
from Features import calculateWavelength
from Features import zeroCrossingRate
from Features import calculateAbsMean
def SignalProcessing_RealtimePatRec(data, patRec):
    # Get signal features
    selFeatures = [item[0][0] for item in patRec[0][0]["selFeatures"]]
    sF  = patRec["sF"][0][0][0][0]
    tFeatures = GetSigFeatures(data,sF,selFeatures)
    result_matrix = np.zeros(12)

    for i in range(4):
        segment_data = [row[i] for row in data]
      
        result_matrix[i] = calculateWavelength(segment_data)
        result_matrix[i + 4] = zeroCrossingRate(segment_data) 
        result_matrix[i + 8] = calculateAbsMean(segment_data) 
    tSet = result_matrix

    # Create a vector with the signal features
    #tSet = np.array([])  # Initialize an empty array
    #for i in range(len(selFeatures)):
    #    feature_name = selFeatures[i]
    #    tSet = np.concatenate((tSet, tFeatures[feature_name]), axis=None)


    # Normalize if required
    
    #tSet = NormalizeSet(tSet, patRec)
    
    # Apply Feature Reduction (PCA) if required
    #tSet = ApplyFeatureReduction(tSet, patRec)
    

    return tSet

