

from Timer import timer

def processor(funcs, inresult=False, get_result=False): # {add():[[1, 2, 3], [1, 2, 3]]}
    from multiprocessing import Pool
    import os
    from functools import wraps
    import time
    def proc(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if __name__ == '__main__':
                with Pool(int(os.environ["NUMBER_OF_PROCESSORS"])) as exe:
                    s = time.time()
                    processes = list()
                    for (i, j) in zip(funcs.keys(), funcs.values()):
                        if get_result is False:
                            processes.append(exe.starmap_async(i, j))
                        else:
                            if __name__ == "__main__":
                                processes.append(exe.starmap_async(i, j).get())
                    f = time.time()
                    print("= "*6, f-s)
                    if inresult is False:
                        return processes
                    else:
                        return func(*args, **kwargs), processes
        return wrapper
    return proc





def foo(a, b):
    return pow(a, b)


if __name__ == '__main__':
    @processor({foo: [[123, 321] for _ in range(1000)],
                pow:[[123, 321] for i in range(10)]}, get_result=False)
    def foo_2():
        pass
    print(foo_2())

    @timer()
    def fooer():
        for i in range(1000):
            pow(123, 321)
    fooer()







