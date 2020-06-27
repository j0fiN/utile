import threading
from functools import wraps
from concurrent.futures import ThreadPoolExecutor
from Timer import timer


def threader(funcs):  # {add():[1, 2, 3]}

    def th(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            with ThreadPoolExecutor(max_workers=len(funcs.keys())) as exe:
                def processes():
                    for (i, j) in zip(funcs.keys(), funcs.values()):
                        yield exe.submit(i, *j)

                #print(list(processes()))
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
    @threader({pow: [123, 321]})
    def foo():pass


    print(len(foo()))
