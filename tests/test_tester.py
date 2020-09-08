import unittest
import sys

sys.path.append('..')
import utile # noqa


class TestTester(unittest.TestCase):

    @utile.Tester.tester(return_test={
        'value': 42,
        'type': int
    })
    def sample_tester_int(self, **_):
        return 42

    def test_tester_1(self):
        self.assertEqual(self.sample_tester_int(test=True)[1], {'value': 42, 'type': int})


if __name__ == '__main__':
    unittest.main()
