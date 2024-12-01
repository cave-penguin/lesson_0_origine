import unittest
import test_calc
import test_new_calk


calkST = unittest.TestSuite()
# calkST.addTest(unittest.makeSuite(test_calc.CalkTest))
calkST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_calc.CalkTest))
calkST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_new_calk.NewCalkTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calkST)