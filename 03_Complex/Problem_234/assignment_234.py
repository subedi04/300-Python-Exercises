'''
Write a Pandas program to create a subset of a given series. 
Add some modification.
'''

import pandas as pd


data = {'A': 10, 'B': 20, 'C': 30, 'D': 40}
original_series = pd.Series(data)

# Create a subset of the Series containing only selected elements
subset_series = original_series[['A', 'C']]

# Print the original and subset Series
print("Original Series:")
print(original_series)

print("\nSubset Series:")
print(subset_series)

# Modify the subset Series
subset_series['A'] = 50

print("\nModified Subset Series:")
print(subset_series)
