import threading
from functools import wraps
from concurrent.futures import ThreadPoolExecutor
from Timer import timer


def threader(funcs):  # {add():[[1, 2, 3], [1, 2, 3]]}

    def th(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            workers = 0
            for arg in funcs.values(): workers = workers + len(arg)

            with ThreadPoolExecutor(max_workers=workers) as exe:
                def processes():
                    for (i, j) in zip(funcs.keys(), funcs.values()):
                        for k in j:
                            yield exe.submit(i, *k)

                # print(list(processes()))
                results = list()
                for process in processes():
                    try:
                        # TODO:Remove 120
                        results.append(process.result(timeout=120))
                    except TimeoutError:
                        raise Exception("Time Limit Exceeded...")
            return results
        return wrapper
    return th


if __name__ == '__main__':


    @timer(store=False)
    @threader({pow: [[123, 321] for _ in range(10000)]})
    def foo(): pass
    foo()
