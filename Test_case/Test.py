import pandas as pd
import matplotlib.pyplot as plt
import unittest
class TestOlympicsData(unittest.TestCase):

    def setUp(self):
        # Setup code to read the CSV files
        self.df_noc = pd.read_csv("noc_regions.csv")
        self.df_selected = pd.read_csv("athlete_events_selected.csv")
        self.df_selected["Medal"] = self.df_selected["Medal"].fillna("No Medal")

    def test_read_csv(self):
        # Test if the CSV files are read correctly
        self.assertFalse(self.df_noc.empty, "NOC regions data should not be empty")
        self.assertFalse(self.df_selected.empty, "Athlete events data should not be empty")

    def test_merged_columns(self):
        # Test if the merged DataFrame has the expected columns
        expected_columns = ["Name", "Sex", "Age", "Sport", "Season", "Year", "Team", "NOC", "region", "Medal", "Height", "Weight"]
        self.assertTrue(all(column in self.df_selected.columns for column in expected_columns), "Merged DataFrame should have the expected columns")

    def test_fillna_medal(self):
        # Test if the 'Medal' column is filled with "No Medal" for missing values
        self.assertTrue((self.df_selected["Medal"] != "").all(), "Medal column should not have empty values")
        self.assertTrue((self.df_selected["Medal"] == "No Medal").sum() > 0, "Medal column should have 'No Medal' for missing values")

    def test_groupby_medal_count(self):
        # Test if the grouping and counting of medals work correctly
        medal_count = self.df_selected.groupby(["NOC", "Season", "Sport"])["Medal"].value_counts().unstack(fill_value=0)
        self.assertFalse(medal_count.empty, "Medal count DataFrame should not be empty")
        self.assertTrue("No Medal" in medal_count.columns, "Medal count DataFrame should have 'No Medal' column")

if __name__ == '__main__':
    unittest.main()