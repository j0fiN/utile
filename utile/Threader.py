
def threader(funcs, func_result=False):
    """
    A Frame-Determined decorator to spring up number of I/O bound tasks.

    Arguments:
        funcs: type: dict holding all your task(s) in form of {my_function: [[] of parameters]}.
        func_result: type: boolean True to return function's return value.

    Returns:
        List of return value(s) of all the I/O bound task(s) (specified within decorator) if func_result = False.
        Tuple containing function's return value and the list respectively if func_result = True.

    Example:
        import requests
        from utile.Threader import threader


        def get_requester(endpoint):
            return requests.get(f"https://localhost:5000/api{endpoint}").text # A sample Api request


        def open_file(name):
            with open(name, "r") as open_file: # A sample file reader
                return open_file.read()


        @threader({get_requester: [["/users/1"], ["/country/India"], ["/profile/pic"]],
                   open_file: [["text.txt"]]})
        def foo(): pass
        foo()

    """
    from functools import wraps
    from concurrent.futures import ThreadPoolExecutor, as_completed
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
                for process in as_completed(processes()):
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
