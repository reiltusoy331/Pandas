# Pandas selecting multiple columns in range
# Read csv file in Pandas

import pandas as pd

# Input the csv file
df = pd.read_csv("C:\\Users\\qwerty\\Documents\\Python Pandas\\Students.csv")

print("Our Dataframe \n", df)

print()

result = df[df.columns[0:3]]

print("Selecting Columns in Range\n")

#Retrieve the 2 columns
print(result)

