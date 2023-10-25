from PatRec_SingleClassifier import PatRec_SingleClassifier

def OneShotPatRecClassifier(patRec, x):
    if patRec["topology"] == "Single Classifier":
        outMov, outVector = PatRec_SingleClassifier(patRec, x)

    
    return outMov, outVector
