import unittest

import mdptest


class MdpTest(unittest.TestCase):
    
    def test_checkPwd(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test2_checkPwd(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test3_checkPwd(self):
        s = '


if __name__ == '__main__':
    unittest.main()

