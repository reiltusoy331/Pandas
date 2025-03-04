# Pandas iterate each columns

import pandas as pd

#Dataset 
Bulls  = {
    'Player':["Kerr","Jordan","Pippen","Rodman","Longley"],
    'Jersey':["25","23","33","91","13",],
    'DraftedYr':['1988','1983','1987','1981','1990']    
}

#DataFrame
Bulls_LineUp = pd.DataFrame(Bulls)

print("Chicago Bulls Roster Dataframe\n",Bulls_LineUp)

print("\n Iterate to each columns")
print()

for index, column in Bulls_LineUp.items():
    print(index)
    print(column)    