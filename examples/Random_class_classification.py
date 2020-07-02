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
from utile.Processor import processor  # noqa
from utile.Timer import timer  # noqa

data_frame = load_iris()
input_data = data_frame.data
data_targets = data_frame.target
X_train, X_test, y_train, y_test = train_test_split(input_data, data_targets, test_size=0.2)

model_knc = KNeighborsClassifier(n_neighbors=5)
model_svc = SVC()
model_rfc = RandomForestClassifier(n_estimators=10)
model_gnb = GaussianNB()
model_mnb = MultinomialNB()


def knc_modeler():
    model_knc.fit(X_train, y_train)
    print(model_knc.score(X_test, y_test))


def svc_modeler():
    model_svc.fit(X_train, y_train)
    print(model_svc.score(X_test, y_test))


def rfc_modeler():
    model_rfc.fit(X_train, y_train)
    print(model_rfc.score(X_test, y_test))


def gnb_modeler():
    model_gnb.fit(X_train, y_train)
    print(model_gnb.score(X_test, y_test))


@timer()
@processor({knc_modeler: [[]],
            svc_modeler: [[]],
            rfc_modeler: [[]],
            gnb_modeler: [[]]}, get_result=True)
def fitter():
    pass


@timer()
def brute_force():
    brute_result = list()
    models = [KNeighborsClassifier(n_neighbors=5), SVC(), RandomForestClassifier(n_estimators=10), GaussianNB()]
    for mod in models:
        model = mod
        model.fit(X_train, y_train)
        brute_result.append(model.score(X_test, y_test))
    return brute_result


if __name__ == '__main__':
    result = fitter()
    print(brute_force())
