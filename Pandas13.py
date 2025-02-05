# Pandas Series name attribute

import pandas as pd

data = [10,20,30,40,50]

dataseries = pd.Series(data,name="Randome Sample")

print("The Pandas series.\n",dataseries)

print(f"Pandas \"name\" attribute in this series is \"{dataseries.name}.\"")

