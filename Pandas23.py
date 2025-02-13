# Pandas Indexing using iloc[] operator
# Read csv file in Pandas

import pandas as pd

# Input the csv file
df = pd.read_csv("C:\\Users\\qwerty\\Documents\\Python Pandas\\Students.csv",index_col="Students")

print("Our Dataframe \n", df)

print()

#Retrieve the 2nd index\row
result = df.iloc[2]

print(f"The retrieved the 2nd index using iloc operator\n", result)
