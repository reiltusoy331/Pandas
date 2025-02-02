# Concatenate DataFrames
import pandas as pd

#Dataset 1
Bulls  = {
    'Player':["Kerr","Jordan","Pippen","Rodman","Longley"],
    'Jersey':["25","23","33","91","13",]
}

#Dataset 2 
Lakers  = {
    'Player':["Fisher","Bryant","Odom","Ariza","Gasul"],
    'Jersey':["2","24","7","3","16"]
}

dataframe1 = pd.DataFrame(Bulls,index=['Player1','Player2','Player3','Player4','Player5'])
print("Chicago Bulls\n",dataframe1) 

dataframe2 = pd.DataFrame(Lakers,index=['Player6','Player7','Player8','Player9','Player10'])
print("\nLA Lakers\n",dataframe2) 

concatDF = pd.concat([dataframe1,dataframe2])
print("\n Concatenated Two Dataframes.\n",concatDF)