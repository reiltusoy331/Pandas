# Pandas adding column to a DataFrame using insert() method

import pandas as pd

#Dataset 
Bulls  = {
    'Player':["Kerr","Jordan","Pippen","Rodman","Longley"],
    'Jersey':["25","23","33","91","13",]    
}

#DataFrame
Bulls_LineUp = pd.DataFrame(Bulls)

print("The Bulls Roster \n",Bulls_LineUp)

#add a new column
Bulls_LineUp.insert(2,"Drafted Yr",['1988','1983','1987','1981','1990'])

print("\nUpdated DataFrame with additional column")
print(Bulls_LineUp)