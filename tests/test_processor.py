import unittest
import sys

sys.path.append('..')
from utile.Processor import processor  # noqa
from utile.Timer import timer  # noqa


class MyTestCase(unittest.TestCase):

    @processor({pow: [[123, 321] for _ in range(10000)]}, func_result=False, get_result=False)
    def sample_p_1(self):
        return None

    @timer()
    @processor({pow: [[123, 321] for _ in range(10000)]}, func_result=False, get_result=True)
    def sample_p_2(self):
        return None

    @processor({pow: [[123, 321] for _ in range(10000)]}, func_result=True, get_result=False)
    def sample_p_3(self):
        return None

    @processor({pow: [[123, 321] for _ in range(10000)]}, func_result=True, get_result=True)
    def sample_p_4(self):
        return None

    @processor({sum: [[123, 321] for _ in range(10000)],
                pow: [[123, 321] for _ in range(10000)]}, func_result=True, get_result=True)
    def sample_p_5(self):
        return None

    def test_1(self):
        result = self.sample_p_1()
        self.assertEqual(str(type(result[0])), "<class 'multiprocessing.pool.MapResult'>")

    def test_2(self):
        result = self.sample_p_2()
        self.assertEqual(str(type(result[0][0])), "<class 'int'>")
        self.assertEqual(result[0][0], 123 ** 321)

    def test_3(self):
        result = self.sample_p_3()
        self.assertEqual(str(type(result[0])), "<class 'NoneType'>")

    def test_4(self):
        result = self.sample_p_4()
        self.assertEqual(str(type(result[1][0][0])), "<class 'int'>")

    def test_5(self):
        result = self.sample_p_4()
        self.assertEqual(str(type(result[0])), "<class 'NoneType'>")
        self.assertEqual(str(type(result[1])), "<class 'list'>")
        self.assertEqual(str(type(result[1][0])), "<class 'list'>")
        self.assertEqual(str(type(result[1][0][0])), "<class 'int'>")


if __name__ == '__main__':
    unittest.main()
