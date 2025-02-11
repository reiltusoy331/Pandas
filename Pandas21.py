# Pandas Indexing
# Read csv file in Pandas


import pandas as pd

# Input the csv file
df = pd.read_csv("C:\\Users\\qwerty\\Documents\\Python Pandas\\Students.csv",index_col="Students")

# print("Our Dataframe \n", df)


#Indexing operators

result = df["Marks"]


print("Our Dataframe \n", result)
