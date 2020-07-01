# Documentation
---
## @timer(store=False, round_off=10)
> **Decorator which print execution time of any function.**

##### Arguments:
**store:**  storing your execution time(`store=True`) or just print it.  
**round_off:** decimals to round off the execution time.

##### Returns:
**Tuple** containing return value and the execution time if `store=True.`  
Returns function's value if `store=False`
---
## @threader(funcs, func_result=False)
> **A Frame-Determined decorator to spring up number of I/O bound tasks.**

##### Arguments:
**funcs:** dictionary holding all your tasks in form of `{my_function:[list of parameters]}`.  
**func_result:** type:boolean True to return function's return value.

##### Returns:
return a **list** of return value(s) of all the I/O bound tasks(specified in decorator) if func_result = False.  
Otherwise returns a **tuple** containing return value and the list respectively.
