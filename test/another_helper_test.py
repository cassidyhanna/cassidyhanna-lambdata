#  test/another_helper_test.py


from Lambdata.helper import CustomFrame


def test_add_state_names():
    custom_df = CustomFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    # assert "name" shouldn't be a column
    # self.assertTrue("Name" not in list(custom_df.columns))
    assert "name" not in list(custom_df.columns)

    custom_df.add_state_name()
    # assert "name" should be a column
    # self.assertTrue("Name" not in list(custom_df.columns))
    assert "name" in list(custom_df.columns)
    # assert "California" should exist in a column called "name"
    # self.assertEqual(custom_df["name"][0], "Cali")
    # self.assertEqual(custom_df["abbrev"][0], "CA")
    assert custom_df["abbrev"][0] == "CA"
    assert custom_df["name"][0] == "Cali"
