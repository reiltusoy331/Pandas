# Name the indexes in a Pandas Series

import pandas as pd

data = [10,20,30,40,50]

dataseries = pd.Series(data,name="Sample Panda Series",index=["Row1","Row2","Row3","Row4","Row5"])

print("# Pandas Series with custom indexes #\n",dataseries) 

print("Indexe: ",dataseries.index) 