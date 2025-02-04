# Access a value in a Pandas Series with Labels

import pandas as pd

data = [10,20,30,40,50]

dataseries = pd.Series(data,index=["Row1","Row2","Row3","Row4","Row5"])

print("# Pandas Series with custom indexes #\n",dataseries) 

print("The value of Row1 is: ",dataseries['Row1'])