import pandas as pd
import numpy as np

# Sample list
my_list = [1, 2, 3, 4, 5]
# Shift elements to the left by one position
shifted_list = my_list[1:] + [my_list[0]]
print(shifted_list)
df = pd.read_csv("olympics_cleaned.csv", header=0)

# Check basic information
print(df.info())

# Display the first few rows
print(df.head())

#list all columns
print(df.columns)

df["Country name"]  # Access 'Country' column
df[["Country name", "Total_Medals"]]  # Access multiple columns
print(df.iloc[0])  # First row (index-based)
print(df.iloc[-1]) # Last row
print(df.iloc[5:10])  # Rows from index 5 to 9
print(df.loc[df["Country name"] == "India"])  # Get India's Olympic stats
"""
# Rename the 'Country' column to 'Country name'
df.rename(columns={'Country': 'Country name'}, inplace=True)

# Create a new column 'Country code' based on the 'Country name' column
df['Country code'] = df['Country name'].apply(lambda x: x.split('(')[-1].replace(')', '').strip() if isinstance(x, str) else '')

# Clean the 'Country name' to remove the code part (e.g., "Afghanistan (AFG)" -> "Afghanistan")
df['Country name'] = df['Country name'].apply(lambda x: x.split('(')[0].strip() if isinstance(x, str) else x)

# Save the cleaned dataset back to the CSV file
df.to_csv('olympics_cleaned.csv', index=False)
"""
# Total medals won in Summer vs. Winter Olympics
print(df.groupby("Summer_Games")["Total_Medals"].sum())

# Add a new column: Total Gold to Total Medals ratio
df["Gold_Medal_Ratio"] = df["Total_Gold"] / df["Total_Medals"]

# Replace missing values (if any) with 0
df.fillna(0, inplace=True)
