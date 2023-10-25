from DiscriminantTest import DiscriminantTest
from ModelTraining import Predict_lda
def OneShotPatRec(patRecTrained, tSet):
    #if patRecTrained['algorithm'] in ['MLP', 'MLP thOut']:
    #    outMov, outVector = MLPTest(patRecTrained, tSet)
    #if patRecTrained['algorithm'] == 'DA':
    outMov ,outVector = Predict_lda(tSet)
    #outMov, outVector = DiscriminantTest(tSet)
    #elif patRecTrained['algorithm'] == 'RFN':
    #    outMov, outVector = RegulationFeedbackTest(patRecTrained['connMat'], tSet.T)
    #elif patRecTrained['algorithm'] == 'SOM':
    #    outMov, outVector = SOMTest(patRecTrained, tSet)
    #elif patRecTrained['algorithm'] == 'SSOM':
    #    outMov, outVector = SSOMTest(patRecTrained, tSet)
    #elif patRecTrained['algorithm'] == 'SVM':
    #    outMov, outVector = SVMTest(patRecTrained, tSet)
    #elif patRecTrained['algorithm'] == 'NetLab MLP':
    #    outMov, outVector = NetLab_MLPTest(patRecTrained, tSet)
    #elif patRecTrained['algorithm'] == 'NetLab GLM':
    #    outMov, outVector = NetLab_GLMTest(patRecTrained, tSet)

    # Validation to prevent outMov from being empty, which may cause problems
    if outMov is None:
        outMov = 0

    return outMov, outVector
