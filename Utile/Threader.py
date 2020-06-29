import threading
from functools import wraps
from concurrent.futures import ThreadPoolExecutor
from Timer import timer


def threader(funcs, inresult=False):  # {add():[[1, 2, 3], [1, 2, 3]]}

    def th(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            workers = 0
            for arg in funcs.values(): workers = workers + len(arg)

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

                if inresult is True:
                    return func(*args, **kwargs), results
                else:
                    return results
        return wrapper
    return th


if __name__ == '__main__':
    pass
