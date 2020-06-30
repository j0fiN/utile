
def threader(funcs, func_result=False):
    from functools import wraps
    from concurrent.futures import ThreadPoolExecutor
    """
    A Frame-Determined decorator to spring up number of I/O bound tasks.

    Arguments:
        funcs: dictionary holding all your tasks in form of {my_function:[list of parameters]}.
        func_result: type:boolean True to return function's return value (default=False).

    Returns:
        return a list of return value(s) of all the the I/O bound tasks(specified in decorator) if func_result = False.
        Otherwise returns a tuple containing return value and the list respectively.

    Example:
        import requests
        from Utile.Threader import threader

        def get_requester(endpoint):
            return requests.get(f"https://localhost:5000/api{endpoint}").json() # A sample Api request

        def open_file(name):
            with open(name, "r") as open_file: # A sample file reader
                return open_file.read()

        @threader({get_requester: [["/users/1"], ["/country/India"], ["/profile/pic"]],
                   open_file: [["text.txt"]]})
        def foo(): pass
        foo()

    """

    def th(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            workers = 0
            for arg in funcs.values():
                workers = workers + len(arg)

            with ThreadPoolExecutor(max_workers=workers) as exe:
                def processes():
                    for (i, j) in zip(funcs.keys(), funcs.values()):
                        for k in j:
                            if str(type(k)) == "<class 'dict'>":
                                yield exe.submit(i, **k)
                            else:
                                yield exe.submit(i, *k)

                results = list()
                for process in processes():
                    try:
                        results.append(process.result())
                    except TimeoutError:
                        raise Exception("Time Limit Exceeded...")

                if func_result is True:
                    return func(*args, **kwargs), results
                else:
                    return results
        return wrapper
    return th
