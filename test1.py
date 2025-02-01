import pandas as pd
import numpy as np

# Sample list
my_list = [1, 2, 3, 4, 5]
# Shift elements to the left by one position
shifted_list = my_list[1:] + [my_list[0]]
print(shifted_list)
df = pd.read_csv("olympics_cleaned.csv", header=1)

# Check basic information
print(df.info())

# Display the first few rows
print(df.head())

#list all columns
print(df.columns)
