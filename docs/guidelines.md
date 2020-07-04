# Guidelines
#### Introduction
> ***There are certain things you need to take into account before you use our package.***  
  
- Have a basic understanding of the concept of *concurrency* and [GIL](https://wiki.python.org/moin/GlobalInterpreterLock) in Python.  
   
- The package is a binding over existing libraries of 
[multiprocessing](https://docs.python.org/3/library/multiprocessing.html), 
[threading](https://docs.python.org/3/library/threading.html) and 
[asynchronous execution](https://docs.python.org/3/library/concurrent.futures.html) to enhance simplistic codeflows for 
your projects.
   
- This package auto tunes the pooling parameters depending on the tasks and your PC specifications. For sophisticated 
pooling and parameter tuning, we highly suggest you to use the base libraries of Python for now. We are bringing in 
advanced parameter tuning within the package soon.  

#### This is about timer decorator
- The timer decorator function was a simple example to show how decorators are being used in the package.
- When the timer decorator is stacked above other decorators, the execution time tends to increase in the power of 
10^(-5) seconds due to sequential execution.

#### This is about threader decorator
- The threader decorator works really slow for tasks which are not I/O bound (please read 
[GIL](https://wiki.python.org/moin/GlobalInterpreterLock)). We highly recommend you to utilize this
decorator only for I/O bound tasks.
- The decorator accepts both arguments and keyword arguments.
- Object's state does NOT change globally when using methods in the decorator.

#### This is about processor decorator
- The processor decorator does not accept keyword arguments for now. We will bring that within the package soon.
- Object's state does NOT change globally when using methods in the decorator.
- Always check if your program is running directly or by some other module using ``if __name__ == "__main__"`` to avoid 
unnecessary errors while running tasks (check
[https://docs.python.org/multiprocessing.html](https://docs.python.org/3/library/multiprocessing.html#using-a-pool-of-workers), 
[https://github.com/](https://github.com/ipython/ipython/issues/10894)).


#### References
- Concurrency in an easy way - [https://youtu.be/iG6fr81xHKA](https://youtu.be/iG6fr81xHKA)
- The mystery of Python - [https://youtu.be/qCGofLIzX6g](https://youtu.be/qCGofLIzX6g), 
[https://youtu.be/IeSu_odkI5I](https://youtu.be/IeSu_odkI5I).  
These are some links that we want to share to change your perception about the Python language as a whole 
(it's magic !!!).

