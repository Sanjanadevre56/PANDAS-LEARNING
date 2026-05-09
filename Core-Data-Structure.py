# Pandas is built on two main data structures:

# Series → One-dimensional (like a single column in Excel)
# DataFrame → Two-dimensional (like a full spreadsheet or SQL table)

import pandas as pd
s = pd.Series([1,2,3,4] , index=["a" ,"b","c","d"])
print(s)

