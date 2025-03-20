# Pandas cleaning data using notnull() function

import pandas as pd


#Input csv file and load in the DataFrame
df = pd.read_csv("C:\\Users\\qwerty\\Documents\\Python Pandas\\CleaningDataDemo.csv")


# Display the csv file records
print("The Original Dataframe\n",df) 

# Find and replace Null with True
resultDataframe = df.notnull()

# Display the new dataframe with no NaN values
print("\nThe Updated Dataframe\n",resultDataframe.to_string()) 