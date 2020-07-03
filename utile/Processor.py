
def processor(funcs: dict, func_result: bool = False, get_result: bool = False) -> function:
    """
    A Frame-Determined decorator to spring up number of CPU bound tasks.

    Arguments:
        funcs: type: dict holding all your task(s) in form of {my_function: [[] of parameters]}.
        func_result: type: boolean True to return function's return value.
        get_result: type: boolean True to return the MapResult object value(s) (process becomes a little slow).

    Returns:
        List of MapResult object(s) of all the CPU bound task(s) with values if get_result = False
        (specified within decorator) and func_result = False.
        Values of CPU bound tasks if get_result = True.
        Tuple containing return value and the list respectively if func_result = True.
        
    Examples:
        from utile.Processor import processor


        def power(a, b):
            return pow(a, b)        # a sample method for computational task


        if __name__ == "__main__":  # important to ensure this.
            @processor({power: [[123, 321] for _ in range(1000)]})
            def foo(): pass
            print(foo())
    """
    from multiprocessing import Pool
    import os
    from functools import wraps

    def proc(func: function) -> function:
        @wraps(func)
        def wrapper(*args: 'arguments', **kwargs: 'keyword arguments') -> function:
            if __name__ == 'utile.Processor' or __name__ == 'Processor':
                with Pool(int(os.environ["NUMBER_OF_PROCESSORS"])) as exe:
                    processes = list()
                    for (i, j) in zip(funcs.keys(), funcs.values()):
                        if get_result is False:
                            exe.starmap_async(i, j).get()
                        else:
                            processes.append(exe.starmap_async(i, j).get())
                    if func_result is False:
                        return processes
                    else:
                        return func(*args, **kwargs), processes

        return wrapper

    return proc
