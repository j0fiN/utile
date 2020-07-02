from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
import numpy as np

import sys
sys.path.append("..")
from Utile.Processor import processor # noqa

data_frame = load_iris()
input_data = data_frame.data
data_targets = data_frame.target
X_train, X_test, y_train, y_test = train_test_split(input_data, data_targets, test_size=0.2)

model_knc = KNeighborsClassifier(n_neighbors=5)
model_svc = SVC()
model_rfc = RandomForestClassifier(n_estimators=10)
model_gnb = GaussianNB()
model_mnb = MultinomialNB()

# @
# def fitter():
#     pass