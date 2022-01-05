import unittest

import mdptest


class TestAll (unittest.TestCase):

    def test_all(self):
        pwd = password()
        testSuite = unittest.TestSuite()
        testResult = unittest.TestResult()
        testSuite.addTest(unittest.makeSuite(pwd.createPassword() ))
        print (testResult.testsRun)
