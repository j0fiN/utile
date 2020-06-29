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


de



if __name__ == '__main__':


    def res(url):
        import requests as r
        return r.get(url=url)


    @processor({time.sleep: [[1], [1]]})
    def foo(): pass

    @timer()
    def fooer(): foo()
    fooer()

    @timer()
    def qwer():
        time.sleep(2)
    qwer()







