
def timer(store: bool = False, round_off: int = 10) -> 'function':
    """
    Decorator which print execution time of any function.

    Arguments:
        store: storing your execution time(store = True) or just print it (store = False).
        round_off: decimals to round off the execution time.

    Returns:
        Tuple containing return value and the execution time if store=True.
        Function's value if store=False.

    Example:
        from utile.Timer import timer
        import time
        @timer()
        def foo():
            time.sleep(1) # function sleeping for 1 second
        foo()
    """
    import time
    from functools import wraps

    def inner_timer(func: 'function') -> 'function':
        @wraps(func)
        def wrapper(*args: 'arguments', **kwargs: 'keyword arguments') -> 'function':
            start_time = time.time()
            value = func(*args, **kwargs)
            finish_time = time.time()
            if store is False:
                print('=' * 100)
                print(f"{func.__name__} function executed in : %s s" % round((finish_time - start_time), round_off))
                print('=' * 100)
                print('\n')
                return value
            else:
                exec_time = round((finish_time - start_time), round_off)
                return value, exec_time

        return wrapper

    return inner_timer
