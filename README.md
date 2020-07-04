# utile
![utile-Logo](https://github.com/j0fiN/Server_Utility/blob/master/docs/utile_logo2.png)
---
*The python package which eases your ```<codeflow>``` using `@decorators`.*
  
---
## Installation
Install with:  
```pip install utile```

For [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb)  
```!pip install utile```
## The art of using decorators
Decorators is one of the many concepts which makes Python programming amazing. The key usage 
of decorators is to modify the functionality or state (behavior) of a function. This package brings out a relatively 
new concept of
**Function Foundation**.  
Function Foundation is a style of programming where a function tends to do nothing and acts like a robust base (or 
foundation) for decorators and these decorators can be made to do sophisticated processes over the idle function.
This (according to us) eases intricate function designing.
## Getting Started
#### @timer() decorator
To compute execution time of a function:
```python
from utile.Timer import timer
import time

@timer()
def foo():
    time.sleep(1)
foo()
```
This will show the execution time(in seconds) irrespective of any print statements.

### Key features of utile

#### @threader() decorator
Provides an easy way to run multiple I/O bound tasks with no hassle of thread pools.
Everything is done for you!
```python
import requests
from utile.Threader import threader


def get_requester(endpoint):
    return requests.get(f"https://localhost:5000/api/{endpoint}").text # sample GET request

@threader({get_requester: [["user/1"], ["user/1/followers"]]})
def foo(): pass
foo()
``` 
The ``@threader()`` decorator takes in a frame-determined structure of all your functions along with its arguments
and returns the list of all the return values of the tasks.

#### @processor decorator
Provides an easy way to run multiple computational tasks with no hassle of Process pools.
Again, Everything is done for you!  
```python
from utile.Processor import processor


def power(a, b):
    return pow(a, b)        # a sample method for computational task


if __name__ == "__main__":  # important to ensure this.
    @processor({power: [[123, 321] for _ in range(10000)]})
    def foo(): pass
    print(foo())
```
The ``@processor()`` decorator takes in a frame-determined structure of all your functions along with its arguments
and returns the list of all the return values of the tasks.

> It's that simple! We take care of all your Pooling and you do your work!

For more information, see [Documentation](http://127.0.0.1:8000/documentation/).
## Contribution
We encourage all the viewers who come up with new ideas using decorators  
to [contribute](https://github.com/) and collaborate (do star the repo if you like it !).

## Licences
The code in this project is licensed under MIT license. See [LICENSE](https://github.com/j0fiN/Server_Utility/blob/master/LICENSE) for more information.



