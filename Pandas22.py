# Pandas Indexing using loc[]
# Read csv file in Pandas

import pandas as pd

# Input the csv file
df = pd.read_csv("C:\\Users\\qwerty\\Documents\\Python Pandas\\Students.csv",index_col="Students")

#Retrieve a single row
result = df.loc["Beckham"]

print("Our Dataframe \n", result)
