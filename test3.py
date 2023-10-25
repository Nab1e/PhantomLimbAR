import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample data with 10 categories, each with 3 features
# You should replace this with your own dataset
# X should be a 2D array where each row represents a data point and each column is a feature.
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [2, 1, 0],
    [5, 4, 3],
    [8, 7, 6],
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7],
    [0, 1, 2]
])

# Corresponding class labels for each data point
# Replace these with your actual class labels
y = np.array([0, 1, 2, 0, 1, 2, 0, 1, 2, 0])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an instance of LDA
lda = LinearDiscriminantAnalysis(n_components=2)  # We reduce to 2 dimensions for visualization

# Fit the LDA model with the training data
lda.fit(X_train, y_train)

# Predict the class labels for the test data
y_pred = lda.predict(X_test)
new_data_point = np.array([[2, 3, 4]])  # Replace this with your new data
predicted_class = lda.predict(new_data_point)
print("Predicted Class:", predicted_class)
# Calculate the accuracy of the LDA model
X_lda = lda.fit_transform(X, y)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
# The transformed data contains 2 components that maximize class separability
print("Transformed data (2 dimensions):\n", X_lda)

# You can access the explained variance ratio to understand the importance of the components
print("Explained Variance Ratio:", lda.explained_variance_ratio_)

# You can also access the coefficients of the linear combination
print("Coefficients (scaling factors for each feature):\n", lda.coef_)

