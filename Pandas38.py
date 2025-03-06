# Pandas checking for duplicate data using duplicated() method

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

print("\n Check for duplicate to each columns")
New_Bulls_LineUp = Bulls_LineUp.duplicated()

print(New_Bulls_LineUp)
