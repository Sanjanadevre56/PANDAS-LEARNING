import pandas as pd
import numpy as np
import sqlite3

data = [
    ["Alice", 25],
    ["Bob", 30],
    ["Charlie", 35]
]

#From python list
df = pd.DataFrame(data , columns=["Name" , "Marks"])
print(df)

#From Dictionary of list
data1 = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}

df1 = pd.DataFrame(data1)

# From Numpy Array
arr = np.array([[1,2,3] , [4,5,6]])
df2 = pd.DataFrame(arr , columns=["A" ,"B" , "C"])
print(df2)

# From CSV Files
df = pd.read_csv("data.csv")

# Use options like:

# sep, header, names, index_col, usecols, nrows, etc.
# Example:

pd.read_csv("data.csv", usecols=["Name", "Age"])

# From Excel Files
# df = pd.read_excel("data.xlsx")

# You may need to install openpyxl or xlrd:

# pip install openpyxl

# From JSON
# df = pd.read_json("data.json")

# Can also read from a URL or string.

# From SQL Databases
 
conn = sqlite3.connect("mydb.sqlite")
df = pd.read_sql("SELECT * FROM users", conn)

# From the Web (Example: CSV from URL)
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# EDA (Exploratory Data Analysis)
# Exploratory Data Analysis (EDA) is an essential first step in any data science project.

# It involves taking a deep look at the dataset to understand its structure, spot patterns, identify anomalies, and uncover relationships between variables. This process includes generating summary statistics, checking for missing or duplicate data, and creating visualizations like histograms, box plots, and scatter plots. The goal of EDA is to get a clear picture of what the data is telling you before applying any analysis or machine learning models.

# By exploring the data thoroughly, you can make better decisions about how to clean, transform, and model it effectively.

# Once your DataFrame is ready, run these to understand your data:

# df.head()         # First 5 rows
# df.tail()         # Last 5 rows
# df.info()         # Column info: types, non-nulls
# df.describe()     # Stats for numeric columns
# df.columns        # List of column names , Attribute
# df.shape          # (rows, columns) , Attribute 

# Summary
# You can create DataFrames from lists, dicts, arrays, files, web, and SQL
# Use .head(), .info(), .describe() to quickly explore any dataset