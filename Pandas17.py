# Pandas Series tail attribute

import pandas as pd

data = [10,20,30,40,50,60,70]

dataseries = pd.Series(data,index=["Row1","Row2","Row3","Row4","Row5","Row6","Row7"])

# tail attibute's default display last 5 rows if value is not specified
print("# Pandas Series display the last three rows #\n",dataseries.tail(3)) 

