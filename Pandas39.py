# Pandas checking for duplicate data using drop_duplicate() method

import pandas as pd

#Dataset 
Bulls  = {
    'Player':["Jordan","Jordan","Pippen","Rodman","Longley"],
    'Jersey':["23","23","33","91","13",],
    'DraftedYr':['1983','1983','1987','1981','1990']    
}

#DataFrame
Bulls_LineUp = pd.DataFrame(Bulls)

print("Chicago Bulls Roster Dataframe\n",Bulls_LineUp)

print("\n Remove\drop duplicate valules")
New_Bulls_LineUp = Bulls_LineUp.drop_duplicates()

print(New_Bulls_LineUp)
