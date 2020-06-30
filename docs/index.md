# Utile

> #### The python package which eases your ```<codeflow>``` using `@decorators`.
  
---
## Installation
Install with:  
```pip install Utile```

For [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb)  
```!pip install Utile```
## Getting Started
If you want to know the execution time of a function:
##### **@timer(store=False, round_off=10)**  
```python
from Utile.Timer import timer
import time

@timer()
def foo():
    time.sleep(1)
foo()
```
This will show the execution time(in seconds) irrespective of any print statements.
