# Pandas Series head attribute

import pandas as pd

data = [10,20,30,40,50,60,70]

dataseries = pd.Series(data,index=["Row1","Row2","Row3","Row4","Row5","Row6","Row7"])

# head attibute's default display the first 5 rows if value is not specified
print("# Pandas Series display the first three rows #\n",dataseries.head(3)) 

