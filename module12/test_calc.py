import random
import unittest

import calk


class CalkTest(unittest.TestCase):
    # def setUp(self):
    #     print("setup")

    # @classmethod
    # def setUpClass(cls):
    #     print("Megasetup")

    # def tearDown(self):
    #     print("teardown")

    # @classmethod
    # def tearDownClass(cls):
    #     print("Megateardown")

    @unittest.skip("Dont like")
    def test_add(self):
        """
        Test for add function in calk
        :return:
        """
        self.assertEqual(calk.add(1, 2), 3)

    @unittest.skipIf(random.randint(0, 2), "No luck")
    def test_sub(self):
        """
        Test for sub function in calk
        :return:
        """
        self.assertEqual(calk.sub(5, 3), 2)

    def test_mul(self):
        """
        Test for mul function in calk
        :return:
        """
        self.assertEqual(calk.mul(5, 3), 15)

    def test_div(self):
        """
        Test for div function in calk
        :return:
        """
        self.assertEqual(calk.div(27, 3), 9)


if __name__ == "__main__":
    unittest.main()
