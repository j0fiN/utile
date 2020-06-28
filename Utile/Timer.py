
"""
Utility on time.
"""
def timer(store, roundoff=10):
    """
    Decorator which print execution time of any function.
    Can be used to measure the response time of a http request.

    :param store: do want to store your execution time(True) or just print it(default=False).
    :param roundoff: decimals to round off the execution time (default is 10).
    if store is true you will get a tuple as return type in your function.
    Usage:

    @timer()
    def foo():
        v_foo = "Hello"
        return v_foo + "World"
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
                print("Response executed in : %s s" % round((finish_time - start_time), roundoff))
                print('=' * 100)
                return value
            else:
                exec_time = round((finish_time - start_time), roundoff)
                return value, exec_time
        return wrapper
    return inner_timer
