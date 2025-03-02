# Pandas sorting the dataframe

import pandas as pd

#Dataset 
Bulls  = {
    'Player':["Kerr","Jordan","Pippen","Rodman","Longley"],
    'Jersey':["25","23","33","91","13",],
    'Drafted Yr':['1988','1983','1987','1981','1990']
}

Bulls_LineUp = pd.DataFrame(Bulls)

print("The Bulls Roster \n",Bulls_LineUp)

print("\n Sorted the Dataframe based on the jersey number in descending order.")


# Sort the dataframe in descending order.

print(Bulls_LineUp.sort_values(by=['Jersey'],ascending=False))



