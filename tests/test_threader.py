import unittest
import sys

sys.path.append('..')
from utile.Threader import threader  # noqa
from utile.Timer import timer  # noqa


def sample_file_reader(name):
    with open(name, "r") as reader:
        return reader.read()


class TestThreader(unittest.TestCase):

    @threader({sample_file_reader: [["sample_test_text.txt"] for _ in range(1000)]}, func_result=True)
    def sample_t_1(self):
        return "Done"

    @threader({sample_file_reader: [["sample_test_text.txt"] for _ in range(1000)]}, func_result=False)
    def sample_t_2(self):
        return "Done"

    def test_1(self):
        result = self.sample_t_1()
        self.assertEqual(str(type(result)), "<class 'tuple'>")

    def test_2(self):
        result = self.sample_t_2()
        self.assertEqual(str(type(result[0])), "<class 'str'>")


if __name__ == '__main__':
    unittest.main()
