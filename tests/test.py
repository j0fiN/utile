import unittest
import sys
import time

sys.path.append('..')
from utile.Threader import threader  # noqa
from utile.Timer import timer  # noqa
from utile.Processor import processor  # noqa
from examples.GET_requester import base, get_requester  # noqa
from examples.iris_flower_classification import knc_modeler, gnb_modeler, svc_modeler, rfc_modeler, fitter  # noqa
from examples.python_blog_scrapper import url_finder, scrape_blog, base  # noqa

unittest.TestLoader.sortTestMethodsUsing = None


def sample_file_reader(name):
    with open(name, "r") as reader:
        return reader.read()


class Test(unittest.TestCase):

    @threader({sample_file_reader: [["sample_test_text.txt"] for _ in range(1000)]}, func_result=True)
    def sample_t_1(self):
        return "Done"

    @threader({sample_file_reader: [["sample_test_text.txt"] for _ in range(1000)]}, func_result=False)
    def sample_t_2(self):
        return "Done"

    def test_1_1(self):
        result = self.sample_t_1()
        self.assertEqual(str(type(result)), "<class 'tuple'>")

    def test_1_2(self):
        result = self.sample_t_2()
        self.assertEqual(str(type(result[0])), "<class 'str'>")

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
        self.assertEqual(str(type(result)), "<class 'list'>")

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

    def test_example_1_base(self):
        s = time.time()
        result = base()
        f = time.time()
        self.assertEqual(str(type(result)), "<class 'list'>")
        self.assertGreater(15, f - s)

    def test_example_1_requester(self):
        self.assertEqual(200, get_requester('https://unsplash.com/photos/A-NVHPka9Rk/download?force=true&w=640'))

    def test_example_2_knc(self):
        self.assertGreater(knc_modeler(), 0.80)

    def test_example_2_svc(self):
        self.assertGreater(svc_modeler(), 0.80)

    def test_example_2_rfc(self):
        self.assertGreater(rfc_modeler(), 0.80)

    def test_example_2_gnb(self):
        self.assertGreater(gnb_modeler(), 0.80)

    def test_example_2_fitter(self):
        self.assertEqual(str(type(fitter())), "<class 'list'>")

    def test_example_3_url_finder(self):
        result = url_finder()
        self.assertEqual(str(type(result)), "<class 'list'>")
        self.assertEqual(str(result[0][0][:5]), "https")

    def test_example_3_scrape_blog(self):
        SAMPLE_URL = 'https://www.fullstackpython.com/blog/report-errors-flask-web-apps-sentry.html'  # scraped
        self.assertEqual(str(type(scrape_blog(SAMPLE_URL))), "<class 'str'>")

    def test_example_3_base(self):
        s = time.time()
        base()
        f = time.time()
        self.assertGreater(60, f - s)
    

if __name__ == '__main__':
    unittest.main()
