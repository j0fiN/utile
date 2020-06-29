from concurrent.futures import ProcessPoolExecutor, as_completed
from Timer import timer
from functools import wraps
import time


def processor(funcs, inresult=False): # {add():[[1, 2, 3], [1, 2, 3]]}

    def proc(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            workers = 0
            for arg in funcs.values(): workers = workers + len(arg)


            if __name__ == '__main__':
                with ProcessPoolExecutor() as exe:
                    processes = list()
                    for (i, j) in zip(funcs.keys(), funcs.values()):
                        for k in j:
                            if str(type(k)) == "<class 'dict'>":
                                processes.append(exe.submit(i, **k))
                            else:
                                processes.append(exe.submit(i, *k))
                    result = list()
                    for process in as_completed(processes):
                        result.append(process.result())

                    if inresult is False:
                        return result
                    else:
                        return func(*args, **kwargs), result
        return wrapper
    return proc


def manyprocessor(funcs): # {funcs:[[], [], []]}

    def mproc(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            with ProcessPoolExecutor() as exe:
                processes = list()
                results = list()
                s = time.time()
                arg = funcs[list(funcs.keys())[0]]
                for i in arg:
                    processes.append(exe.submit(list(funcs.keys())[0], *i))
                for process in processes:
                    results.append(process.result())
                f = time.time()
                print(results, " = ", f-s)
                return results
        return wrapper
    return mproc





if __name__ == '__main__':

    @timer()
    @manyprocessor({pow:[[123, 321] for _ in range(1000)
                         ]})
    def foo(): pass
    foo()

    @timer()
    def fooer():
        for i in range(1000):
            pow(123, 321)
    fooer()
    # import os
    # print(int(os.environ["NUMBER_OF_PROCESSORS"]))







