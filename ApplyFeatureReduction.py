import PCATest

def ApplyFeatureReduction(x, patRec):
    ftR = patRec["featureReduction"][0][0][0][0][0][0]
    if ftR == 'PCA':
        x = PCATest(x, patRec.featureReduction.eigVecTrData, patRec.selFeatures)
    return x