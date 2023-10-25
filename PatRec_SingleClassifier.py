from OneShotPatRec import OneShotPatRec
def PatRec_SingleClassifier(patRec, x):
    outMov, outVector = OneShotPatRec(patRec['patRecTrained'], x)
    return outMov, outVector