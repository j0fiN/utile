from functools import wraps
from concurrent.futures import ThreadPoolExecutor

"""
log = {
        0:
            {
                'endpoint':"value",
                'execution_time':"value",
                'response_code':"value",
                'content': "value"
            }
    }

"""

# `GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``

from Timer import timer


def getendtest(endpoints):
    import requests

    def end(func):
        @wraps(func)
        def wrapper(**kwargs):
            try:
                url = kwargs['url']
                requests.get(url=url)
            except KeyError:
                raise Exception("Invalid default parameter. Use 'url' as your default parameter.")
            except ConnectionError:
                raise Exception("Unresponsive base Url...")

            log = dict()

            @timer(True)
            def responser(url):
                return requests.get(url=url)

            with ThreadPoolExecutor(max_workers=len(endpoints)) as exe:
                processes = list()
                for endpoint in endpoints:
                    processes.append(exe.submit(responser, url + endpoint))

                for i, (future, endpoint) in enumerate(zip(processes, endpoints)):
                    log[i] = dict()
                    log[i]['endpoint'] = endpoint
                    log[i]['execution_time'] = future.result()[1]
                    response = future.result()[0]
                    log[i]['response_code'] = response.status_code
                    log[i]['content'] = response.content
            return log
        return wrapper
    return end


if __name__ == '__main__':
    @timer(False)
    @getendtest(
        endpoints=['country/India', 'region/Asia', '/update', "country/Germany", "country/Canada", "country/France"])
    def res(url):
        pass


    log = res(url="https://covid-api-19.glitch.me/api/notildore2020/")
    s = 0
    for i in log.values():
        s = s + i['execution_time']

    print("original time = ", s, "sec")
