# test/helper_test.py

import unittest

from Lambdata.helper import CustomFrame


class test_CustomFrame(unittest.TestCase):

    def test_add_state_names(self):
        custom_df = CustomFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
        # assert "name" shouldn't be a column
        self.assertTrue("Name" not in list(custom_df.columns))

        custom_df.add_state_name()
        # assert "name" should be a column
        self.assertTrue("Name" not in list(custom_df.columns))
        # assert "California" should exist in a column called "name"
        # self.assertEqual(True, True)
        self.assertEqual(custom_df["name"][0], "Cali")
        self.assertEqual(custom_df["abbrev"][0], "CA")


if __name__ == '__main__':
    unittest.main()
