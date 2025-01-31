# Join DataFrames 
import pandas as pd

#Dataset 1
Bulls  = {
    'Player':["Kerr","Jordan","Pippen","Rodman","Longley"],
    'Jersey':["25 ","23 ","33 ","91 ","13 ",]
}

#Dataset 2 
Rings = {
    'Year ':[1991,1992,1993,1996,1997],
    'Record':["61-21","67-15","57-25","72-10","69-13"]
}


dataframe1 = pd.DataFrame(Bulls)
dataframe1.index = range(1,len(dataframe1)+1)
print("Chicago Bulls\n",dataframe1)


print()

dataframe2 = pd.DataFrame(Rings)
dataframe2.index = range(1,len(dataframe2)+1)
print("Championships\n",dataframe2)


combineDF = dataframe1.join(dataframe2)

print("\n The Chicago Bulls Dynasty \n",combineDF)