import unittest
import sys
import time
import requests
sys.path.append("..")
from examples.GET_requester import base, get_requester # noqa


class MyTestCase(unittest.TestCase):

    def test_example_base(self):
        s = time.time()
        result = base()
        f = time.time()
        self.assertEqual(str(type(result)), "<class 'list'>")
        self.assertGreater(15, f-s)

    def test_example_1_requester(self):
        self.assertEqual(200, get_requester('https://unsplash.com/photos/A-NVHPka9Rk/download?force=true&w=640'))


if __name__ == '__main__':
    unittest.main()
