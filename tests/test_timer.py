import unittest
import time
from Utile.Timer import timer


class MyTestCase(unittest.TestCase):

    def test_returns_1(self):
        self.sample_2()
        self.assertEqual(None, self.sample_2())

    def test_returns_2(self):
        result = self.sample_1()[1]
        self.assertAlmostEqual(0.5, result, 1)

    def test_doc(self):
        help(timer)

    @timer(True)
    def sample_1(self):
        time.sleep(0.5)
        return None

    @timer(store=False)
    def sample_2(self):
        time.sleep(0.5)
        return None



if __name__ == '__main__':
    unittest.main()
