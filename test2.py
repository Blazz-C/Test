import pandas as pd
import numpy as np

df_athletes = pd.read_csv("athlete_events.csv")  # Athlete data
df_noc = pd.read_csv("noc_regions.csv")  # NOC regions data
df_selected = pd.read_csv("athlete_events_selected.csv")  # Selected columns
"""
# Merge the two datasets on 'NOC' column
df_merged = pd.merge(df_athletes, df_noc, on='NOC', how='left')

# Display the first few rows
print(df_merged.head())    

df_selected = df_merged[["Name", "Sex", "Age", "Sport","Season","Year","Team" ,"NOC", "region","Medal","Height","Weight"]]

# Save the selected columns to a new CSV file
df_selected.to_csv('athlete_events_selected.csv', index=False)
"""
# Display the first few rows of the new dataset
print(df_selected.head())
df_selected["Medal"] = df_selected["Medal"].fillna("No Medal")  
# Group by 'NOC', 'Season', and 'Sport' columns and count the number of medals
medal_count = df_selected.groupby(["NOC", "Season", "Sport"])["Medal"].value_counts().unstack(fill_value=0)

print(medal_count)

medal_count.to_csv('medal_count.csv')  # Save the medal count to a new CSV file

