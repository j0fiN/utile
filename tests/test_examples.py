import unittest
import sys
import time
sys.path.append("..")
from examples.GET_requester import base, get_requester # noqa
from examples.iris_flower_classification import knc_modeler # noqa


class MyTestCase(unittest.TestCase):

    def test_example_1_base(self):
        s = time.time()
        result = base()
        f = time.time()
        self.assertEqual(str(type(result)), "<class 'list'>")
        self.assertGreater(15, f-s)

    def test_example_1_requester(self):
        self.assertEqual(200, get_requester('https://unsplash.com/photos/A-NVHPka9Rk/download?force=true&w=640'))

    def test_example_2_kns(self):
        self.assertGreater(kns_modeler(), 0.85)

    def test_example_2_svc(self):
        self.assertGreater(svc_modeler(), 0.85)

    def test_example_2_rfc(self):
        self.assertGreater(rfc_modeler(), 0.85)

    def test_example_2_gnb(self):
        self.assertGreater(gnb_modeler(), 0.85)


if __name__ == '__main__':
    unittest.main()
