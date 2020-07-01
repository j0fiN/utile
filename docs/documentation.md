# Documentation
---
## @Timer.timer(store=False, round_off=10)
> **Decorator which print execution time of any function.**

##### Arguments:
**store:**  storing your execution time(`store = True`) or just print it (`store = False`).  
**round_off:** decimals to round off the execution time.

##### Returns:
**Tuple** containing return value and the execution time if `store = True`.  
Function's return value if `store = False`.
---
## @Threader.threader(funcs, func_result=False)
> **A Frame-Determined decorator to spring up number of I/O bound tasks.**

##### Arguments:
**funcs:** type: **dict** holding all your tasks in form of `{my_function: [list of parameters]}`.  
**func_result:** type: **boolean** `True` to return function's return value.

##### Returns:
**List** of return value(s) of all the I/O bound tasks (specified within decorator) if `func_result = False`.  
**Tuple** containing function's return value and the list respectively if `func_result = True`.
---
## @Processor.processor(funcs, func_result=False, get_result=False)
> **A Frame-Determined decorator to spring up number of CPU bound tasks.**

###### Arguments:
**funcs:** type: **dict** holding all your tasks in form of `{my_function: [list of parameters]}`.  
**func_result:** type: **boolean** `True` to return function's return value.  
**get_result:** type: **boolean** `True` to return the MapResult object values (process becomes little slow than usual).

##### Returns:
**List** of MapResult object(s) of all the CPU bound tasks with values if `get_result = False` (specified within decorator) 
and `func_result = False`.  
Values of CPU bound tasks if `get_result = True`.  
**Tuple** containing return value(s) and the list respectively if `func_result = True`.