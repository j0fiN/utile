
def timer(store=False, round_off=10):
    """
    Decorator which print execution time of any function.

    Arguments:
        store:  storing your execution time(store=True) or just print it.
        round_off: decimals to round off the execution time (default=10).

    Returns:
        Tuple containing return value and the execution time if store=True.
        Return value if store=False

    Example:
        from Utile.Timer import timer
        import time
        @timer()
        def foo():
            time.sleep(1) # function sleeping for 1 second
        foo()
    """
    import time
    from functools import wraps

    def inner_timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
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
