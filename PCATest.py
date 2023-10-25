import numpy as np

def PCATest(inputData, eigVecTrData, selFeatures):
    recData = inputData[:, selFeatures].reshape(-1, len(selFeatures))
    PCAData = np.dot(recData, eigVecTrData)
    PCAData = PCAData.reshape(inputData.shape[0], -1)
    return PCAData
