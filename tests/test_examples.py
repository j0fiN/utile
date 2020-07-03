import unittest
import sys
import time
sys.path.append("..")
from examples.GET_requester import base, get_requester # noqa
from examples.iris_flower_classification import knc_modeler, gnb_modeler, svc_modeler, rfc_modeler, fitter # noqa


class MyTestCase(unittest.TestCase):

    def test_example_1_base(self):
        s = time.time()
        result = base()
        f = time.time()
        self.assertEqual(str(type(result)), "<class 'list'>")
        self.assertGreater(15, f-s)

    def test_example_1_requester(self):
        self.assertEqual(200, get_requester('https://unsplash.com/photos/A-NVHPka9Rk/download?force=true&w=640'))

    def test_example_2_knc(self):
        self.assertGreater(knc_modeler(), 0.85)

    def test_example_2_svc(self):
        self.assertGreater(svc_modeler(), 0.85)

    def test_example_2_rfc(self):
        self.assertGreater(rfc_modeler(), 0.85)

    def test_example_2_gnb(self):
        self.assertGreater(gnb_modeler(), 0.85)

    def test_example_2_fitter(self):
        self.assertEqual(str(type(fitter())), "<class 'list'>")


if __name__ == '__main__':
    unittest.main()
