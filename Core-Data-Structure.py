# Pandas is built on two main data structures:

# Series → One-dimensional (like a single column in Excel)
# DataFrame → Two-dimensional (like a full spreadsheet or SQL table)

import pandas as pd

# Series — 1D Labeled Array
s = pd.Series([1,2,3,4] , index=["a" ,"b","c","d"])
print(s)

# DataFrame - 2D Labeled Table
df = pd.DataFrame([1,2,3,4])
print(df)

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["Delhi", "Mumbai", "Bangalore"]
}

dframe = pd.DataFrame(data)
print(dframe)

# Index and Labels
# Every Series and DataFrame has an Index — it helps with:

# Fast lookups
# Aligning data
# Merging & joining
# Time series operations
# df.index         # Row labels
# df.columns       # Column labels

# You can change them using:

df.index = ["a", "b", "c"]
df.columns = ["Name", "Age", "City"]

# Why Learn These Well?
# Most Pandas operations are built on these foundations:

# Selection
# Filtering
# Merging
# Aggregation
# Understanding Series & DataFrames will make everything else easier.

# Summary
# Series = 1D array with labels
# DataFrame = 2D table with rows + columns
# Both come with index and are the heart of Pandas