# Pandas iterate over rows method 1

import pandas as pd

#Dataset 
Bulls  = {
    'Player':["Kerr","Jordan","Pippen","Rodman","Longley"],
    'Jersey':["25","23","33","91","13",],
    'Drafted Yr':['1988','1983','1987','1981','1990']
}

Bulls_LineUp = pd.DataFrame(Bulls)

print("The Bulls Roster \n",Bulls_LineUp)

print("\n")

# Iterate over the rows using iterrows() method
for row in Bulls_LineUp.iterrows():
    print("\n",row)


