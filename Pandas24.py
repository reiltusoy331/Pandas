# Pandas selecting multiple columns
# Read csv file in Pandas

import pandas as pd

# Input the csv file
df = pd.read_csv("C:\\Users\\qwerty\\Documents\\Python Pandas\\Students.csv")

print("Our Dataframe \n", df)

print()

result = df[['Students','Age']]

print("Selecting Two Columns\n")

#Retrieve the 2 columns
print(result)

