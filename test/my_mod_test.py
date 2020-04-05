# test/my_mod_test.py

import unittest

from Lambdata.my_mod import enlarge


class TestMyMod(unittest.TestCase):

    def test_enlarge(self):
        self.assertEqual(enlarge(5), 500)


if __name__ == '__main__':
    unittest.main()
