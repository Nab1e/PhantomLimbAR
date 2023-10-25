
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score
import joblib  # Import joblib for model persistence

# Assuming 'result_matrix' is your list of NumPy arrays where each array represents a class.
# 'result_matrix' should be a list of shape (31, 12) for 10 classes.
def ModelTraining(result_matrix,n):
    # Initialize arrays to store features and labels from all classes.
    allFeatures = []
    allLabels = []

    # Populate 'allFeatures' and 'allLabels' by extracting data from 'result_matrix'.
    for classIdx, class_data in enumerate(result_matrix, 1):
        numDataPoints, numFeatures = class_data.shape

        # Create labels for this class (classIdx).
        classLabels = np.ones(numDataPoints) * classIdx

        allFeatures.extend(class_data)
        allLabels.extend(classLabels)

    # Convert lists to NumPy arrays
    allFeatures = np.array(allFeatures)
    allLabels = np.array(allLabels)

    # Split the data into training and testing sets
    trainingFeatures, testingFeatures, trainingLabels, testingLabels = train_test_split(allFeatures, allLabels, test_size=0.3, random_state=42)

    # Train an LDA model on the training dataset
    ldaModel = LinearDiscriminantAnalysis(solver='eigen')  # 'eigen' solver is similar to 'pseudoLinear'
    ldaModel.fit(trainingFeatures, trainingLabels)

    # Predict the class labels for the testing data
    predictedLabels = ldaModel.predict(testingFeatures)

    # Evaluate the model's performance by calculating accuracy
    accuracy = accuracy_score(testingLabels, predictedLabels)
    print(f'Accuracy: {accuracy * 100:.2f}%')
    input_data = result_matrix[4][0].reshape(1, -1)
    outMov  = ldaModel.predict(input_data)
    print("Predicted Labels:", outMov )
    joblib.dump(ldaModel, 'lda_model.pkl')

    return ldaModel

def Predict_lda(data):
    ldaModel = joblib.load('lda_model.pkl')

    input_data = data.reshape(1, -1)
    outMov  = ldaModel.predict(input_data)
    print("Predicted Labels:", outMov )
    outVector = 0
    return outMov ,outVector
    # Now, you have 'predictedLabels' containing the predicted class labels for the testing data.

    # You can print the predicted labels or use them as needed.
