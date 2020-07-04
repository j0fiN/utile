# Guidelines
> ***There are certain things you need to take into account before you use our package.***  
  
- Have a basic understanding of the concept of *concurrency* and *GIL* in Python.  
   
- The package is a binding over existing libraries of 
[multiprocessing](https://docs.python.org/3/library/multiprocessing.html), 
[threading](https://docs.python.org/3/library/threading.html) and 
[asynchronous execution](https://docs.python.org/3/library/concurrent.futures.html) to enhance simplistic codeflows for 
your projects.
   
- This package auto tunes the pooling parameters depending on the tasks and your PC specifications. For sophisticated 
pooling and parameter tuning, we highly suggest you to use the base libraries of Python for now. We are bringing in 
advanced parameter tuning within the package soon.  

#### This is about timer decorator

