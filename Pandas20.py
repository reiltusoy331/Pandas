# Read csv file in Pandas
# Display bottom 5 rows of the DataFrame
# tail() method method with a deafult of 5 rows

import pandas as pd

# Input the file
df = pd.read_csv("C:\\Users\\qwerty\\Documents\\Python Pandas\\Students.csv")


#Display the CSV file records
print("# The Students Dataframe #\n")
print("The Top 3 Players of the Season.\n",df.tail(3))