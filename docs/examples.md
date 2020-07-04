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
This example shows web scraping of python blog from
[fullstackpython](https://www.fullstackpython.com/) using beautiful soup python library.

**NOTE:**

- Sometimes even I/O bound tasks work slower than brute force
when using threading, depending on the PC. Use processor at those times.

- This example needs the requests, beautiful soup and html5lib libraries.
```python
# Example - 3

from bs4 import BeautifulSoup
import requests

from utile.Threader import threader
from utile.Timer import timer


def url_finder():
    res = requests.request("GET", url='https://www.fullstackpython.com/blog.html')
    soup = BeautifulSoup(res.content, 'html5lib')
    links = soup.find_all('div', attrs={'class': 'c12'})[1]
    links = links.find_all('div', attrs={'class': 'row'})
    url_list = list()
    for link in links:
        url_list.append(['https://www.fullstackpython.com' + link.find('a')['href']])
    return url_list


def scrape_blog(link):
    response = requests.request("GET", url=link)
    soup = BeautifulSoup(response.content, 'html5lib')
    if soup.find('div', attrs={'class': 'c9'}) is None:
        return None
    else:
        blog = [str(i.text) for i in soup.find('div', attrs={'class': 'c9'}).find_all(['p', 'pre'])]
    return "".join(blog)


@timer()
@threader({scrape_blog: url_finder()})
def base():
    pass


print(base())
```
---
### Notes

- Please see the [Guidelines](http://127.0.0.1:8000/guidelines/) before jumping in.
- For more dynamic usage of the decorator functions, see [Documentation](http://127.0.0.1:8000/documentation/).
- Want to add more examples, feel free to [Contribute](https://github.com/j0fiN).
