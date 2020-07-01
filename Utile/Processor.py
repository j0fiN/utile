def processor(funcs, func_result=False, get_result=False):
    """
    A Frame-Determined decorator to spring up number of CPU bound tasks.
    
    Arguments:
        funcs: dictionary holding all your tasks in form of {my_function:[list of parameters]}.
        func_result: type:boolean True to return function's return value (default=False).
        get_result: type:boolean True to return the MapResult object values (process becomes little slow)(default=False)
        
    Returns:
        return a list of MapResult object(s)(with values if get_result=True) of all the CPU bound 
        tasks(specified in decorator) if func_result = False. Otherwise returns a tuple containing return value(s) 
        and the list respectively.
        
    Examples:
        from Utile.Processor import processor


        def power(a, b):
            return pow(a, b)  # a sample method for CPU  bound task


        if __name__ == "__main__":  # important to ensure this.
            @processor({power: [[123, 321] for _ in range(1000)]})
            def foo(): pass
            print(foo())
    """
    from multiprocessing import Pool
    import os
    from functools import wraps

    def proc(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if __name__ == 'Utile.Processor' or __name__ == 'Processor':
                with Pool(int(os.environ["NUMBER_OF_PROCESSORS"])) as exe:
                    processes = list()
                    for (i, j) in zip(funcs.keys(), funcs.values()):
                        if get_result is False:
                            processes.append(exe.starmap_async(i, j))
                        else:
                            processes.append(exe.starmap_async(i, j).get())
                    if func_result is False:
                        return processes
                    else:
                        return func(*args, **kwargs), processes

        return wrapper

    return proc
