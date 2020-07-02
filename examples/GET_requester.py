# Example - 1
# This example shows a simple multi-threading process using threader
# decorator along with brute force function too.
# NOTE: Sometimes even I/O bound tasks work slower than brute force
# when using threading, depending on the PC. Use processor at those times.
# This example needs the requests module so send GET requests.

import requests
import sys

sys.path.append("..")
from utile.Timer import timer  # noqa
from utile.Threader import threader  # noqa


def get_requester(url):
    result = requests.get(url)
    return result.status_code


@timer()  # there is a lag of about few milliseconds if timer is stacked above. See Guidelines for information.
@threader({get_requester: [['https://unsplash.com/photos/A-NVHPka9Rk/download?force=true&w=640'],
                           ['https://unsplash.com/photos/A-NVHPka9Rk/download?force=true&w=1920'],
                           ['https://unsplash.com/photos/A-NVHPka9Rk/download?force=true&w=2400']]})
def base():
    pass


@timer()
def brute_force():
    endpoints = ['https://unsplash.com/photos/A-NVHPka9Rk/download?force=true&w=640',
                 'https://unsplash.com/photos/A-NVHPka9Rk/download?force=true&w=1920'
                 'https://unsplash.com/photos/A-NVHPka9Rk/download?force=true&w=2400']
    for endpoint in endpoints:
        get_requester(endpoint)


# brute_force()
base()
