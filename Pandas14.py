# Pandas Series hasnans attribute

import pandas as pd
import numpy as np

data = [10,20,30,40,50,np.nan]

dataseries = pd.Series(data,name="Randome Sample")

print("The Pandas series.\n",dataseries)

print(f"Does this Pandas series \"hasnans\" value? -> \"{dataseries.hasnans}\"")

