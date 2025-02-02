import pandas as pd
import pytest

# Load data globally to avoid reloading in every test
df_noc = pd.read_csv("noc_regions.csv")
df_selected = pd.read_csv("athlete_events_selected.csv")
df_selected["Medal"] = df_selected["Medal"].fillna("No Medal")

def test_read_csv():
    """Test if CSV files are read correctly."""
    assert not df_noc.empty, "NOC regions data should not be empty"
    assert not df_selected.empty, "Athlete events data should not be empty"

def test_merged_columns():
    """Test if DataFrame has the expected columns."""
    expected_columns = ["Name", "Sex", "Age", "Sport", "Season", "Year", "Team", "NOC", "region", "Medal", "Height", "Weight"]
    assert all(column in df_selected.columns for column in expected_columns), "Merged DataFrame should have the expected columns"

def test_fillna_medal():
    """Test if the 'Medal' column is correctly filled with 'No Medal'."""
    assert (df_selected["Medal"] != "").all(), "Medal column should not have empty values"
    assert (df_selected["Medal"] == "No Medal").sum() > 0, "Medal column should have 'No Medal' for missing values"

def test_groupby_medal_count():
    """Test grouping and counting of medals."""
    medal_count = df_selected.groupby(["NOC", "Season", "Sport"])["Medal"].value_counts().unstack(fill_value=0)
    assert not medal_count.empty, "Medal count DataFrame should not be empty"
    assert "No Medal" in medal_count.columns, "Medal count DataFrame should have 'No Medal' column"

