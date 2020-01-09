import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

from logistic_regression import LogisticRegression
ds = datasets.load_breast_cancer()
X, y = ds.data, ds.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

def accuracy(y_t, y_pred):
    accuracy = np.sum(y_t == y_pred ) / len(y_t)
    return accuracy

regressor = LogisticRegression(lr=0.0001, n_iters=1000)
regressor.fit(X_train, y_train)
predictions = regressor.predict(X_test)

print("Brest Cancer Accuracy: ", accuracy(y_test, predictions))


