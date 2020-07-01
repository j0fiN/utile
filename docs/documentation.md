# Documentation
---
## @Timer.timer(store=False, round_off=10)
> **Decorator which print execution time of any function.**

##### Arguments:
**store:**  storing your execution time(`store = True`) or just print it.  
**round_off:** decimals to round off the execution time.

##### Returns:
**Tuple** containing return value and the execution time if `store = True`.  
Returns function's value if `store = False`
---
## @Threader.threader(funcs, func_result=False)
> **A Frame-Determined decorator to spring up number of I/O bound tasks.**

##### Arguments:
**funcs:** type: **dict** holding all your tasks in form of `{my_function: [list of parameters]}`.  
**func_result:** type: **boolean** `True` to return function's return value.

##### Returns:
 **List** of return value(s) of all the I/O bound tasks (specified within decorator) if `func_result = False`.  
Returns a **tuple** containing return value and the list respectively if `func_result = True`.
---
## @Processor.processor(funcs, func_result=False, get_result=False)
> **A Frame-Determined decorator to spring up number of CPU bound tasks.**

###### Arguments:
**funcs:** type: **dict** holding all your tasks in form of `{my_function: [list of parameters]}`.  
**func_result:** type: **boolean** `True` to return function's return value.  
**get_result:** type: **boolean** `True` to return the MapResult object values (process becomes little slow than usual).

##### Returns:
**List** of MapResult object(s) of all the CPU bound with values if `get_result=True` tasks (specified within decorator) 
if `func_result = False`.  
Returns a **tuple** containing return value(s) and the list respectively if `func_result = True`.