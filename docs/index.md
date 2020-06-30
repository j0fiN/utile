# Utile

*The python package which eases your ```<codeflow>``` using `@decorators`.*
  
---
## Installation
Install with:  
```pip install Utile```

For [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb)  
```!pip install Utile```
## Getting Started
#### @timer() decorator
To compute execution time of a function:
```python
from Utile.Timer import timer
import time

@timer()
def foo():
    time.sleep(1)
foo()
```
This will show the execution time(in seconds) irrespective of any print statements.

#### @threader() decorator
The key feature of Utile is that it provides an easy way to run multiple I/O bound tasks with no hassle of thread pools.
Everything is done for you!
```python
import requests
from Utile.Threader import threader

def open_file(name):
    with open(name, "r") as open_file: # A sample file reader
        return open_file.read()

@threader({open_file: [["text_1.txt"], ["text_2.txt"]]})
def foo(): pass
foo()
``` 
The ``@threader()`` decorator takes in a frame-determined structure of all your functions along with its arguments
and returns the list of all the return values of the tasks. It's that simple!  
We take care of all your ThreadPooling and you do your work!

## Contribution
Want to make some complex process fast and easy using decorators, feel free to [contribute](https://github.com/).

## Licences
The code in this project is licensed under MIT license. See [LICENSE](https://github.com/j0fiN/Server_Utility/blob/master/LICENSE) for more information.


