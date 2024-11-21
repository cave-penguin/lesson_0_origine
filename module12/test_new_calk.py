import unittest
import calk


class NewCalkTest(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(calk.sqrt(9), 3)

    def test_pow(self):
        self.assertEqual(calk.pow(2, 4), 16)
