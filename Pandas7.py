# Access a value in a Pandas Series

import pandas as pd

data = [10,20,30,40,50]

dataseries = pd.Series(data)

print("# Sample of Pandas Series #\n",dataseries) 

print("Value access in the Series: ",dataseries[1])