import unittest
import time
import sys
sys.path.append('..')
from utile.Timer import timer # noqa


class TestTimer(unittest.TestCase):

    def test_returns_1(self):
        self.assertAlmostEqual(0.5, self.sample_2()[1], 2)

    def test_returns_2(self):
        result = self.sample_1()
        self.assertEqual(str(type(result)), "<class 'tuple'>")

    @timer(True)
    def sample_1(self):
        time.sleep(0.5)
        return None

    @timer(store=True)
    def sample_2(self):
        time.sleep(0.5)
        return None


if __name__ == '__main__':
    unittest.main()
