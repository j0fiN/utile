# Examples
---
### Example - 1
This example shows a simple GET request process using threader
decorator.  
**NOTE:**  

- Sometimes even I/O bound tasks work slower than brute force
  when using threading, depending on the PC. Use processor at those times.  
  
- This example needs the requests module to send GET requests.  

- The links used in this example is from [unsplash](https://unsplash.com/).
  No permission is needed for using them.
```python
# Example - 1

import requests
from utile.Timer import timer
from utile.Threader import threader


def get_requester(url):
    result = requests.get(url)
    return result.status_code


@timer()  # There is a lag of about few milliseconds if timer is stacked above. 
@threader({get_requester: [['https://unsplash.com/photos/A-NVHPka9Rk/download?force=true&w=640'],
                           ['https://unsplash.com/photos/A-NVHPka9Rk/download?force=true&w=1920'],
                           ['https://unsplash.com/photos/A-NVHPka9Rk/download?force=true&w=2400']]})
def base():
    pass


base() 
```
---
### Example - 2
This example shows classification of iris flowers in various
estimators using SciKit-Learn library.

**NOTE:**

- This example requires sk-learn, numpy libraries.
Objects are not made global within the processor, which means
objects does not change its state globally after passing through
the processor decorator.
- To retain the state use get_result=True.
- Always check if your program is running directly or by some other module using
`if __name__ == "__main__": ...`.
```python
# Example - 2

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
import numpy as np

from utile.Processor import processor
from utile.Timer import timer

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
    value = model_knc.score(X_test, y_test)
    return value


def svc_modeler():
    model_svc.fit(X_train, y_train)
    value = model_svc.score(X_test, y_test)
    return value


def rfc_modeler():
    model_rfc.fit(X_train, y_train)
    value = model_rfc.score(X_test, y_test)
    return value


def gnb_modeler():
    model_gnb.fit(X_train, y_train)
    value = model_gnb.score(X_test, y_test)
    return value


@timer()
@processor({knc_modeler: [[]],
            svc_modeler: [[]],
            rfc_modeler: [[]],
            gnb_modeler: [[]]})
def fitter():
    pass


if __name__ == '__main__':  # important to ensure this.
    fitter()
```
---
### Example - 3

