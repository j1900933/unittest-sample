import unittest
import sample

class TestSample(unittest.TestCase):

    def test_add_num(self):
        result = sample.add_num(2, 3)

        self.assertEqual(5, result)