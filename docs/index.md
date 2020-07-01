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

### Key features of Utile

#### @threader() decorator
Provides an easy way to run multiple I/O bound tasks with no hassle of thread pools.
Everything is done for you!
```python
import requests
from Utile.Threader import threader


def open_file(name):
    with open(name, "r") as open_file: # A sample file reader
        return open_file.read()

# Create two text files 'text_1.txt' and 'text_2.txt' before you copy this snippet

@threader({open_file: [["text_1.txt"], ["text_2.txt"]]})
def foo(): pass
foo()
``` 
The ``@threader()`` decorator takes in a frame-determined structure of all your functions along with its arguments
and returns the list of all the return values of the tasks.

#### @processor decorator
Provides an easy way to run multiple computational tasks with no hassle of Process pools.
Again, Everything is done for you!  
```python
from Utile.Processor import processor


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

For more Information, go to the [documentation]()
## Contribution
Want to make some complex process fast and easy using decorators, feel free to [contribute](https://github.com/).

## Licences
The code in this project is licensed under MIT license. See [LICENSE](https://github.com/j0fiN/Server_Utility/blob/master/LICENSE) for more information.


