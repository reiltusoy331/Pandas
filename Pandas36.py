# Pandas removing column to a DataFrame using drop() method

import pandas as pd

#Dataset 
Bulls  = {
    'Player':["Kerr","Jordan","Pippen","Rodman","Longley"],
    'Jersey':["25","23","33","91","13",],
    'DraftedYr':['1988','1983','1987','1981','1990']    
}

#DataFrame
Bulls_LineUp = pd.DataFrame(Bulls)


print("The Bulls Roster \n",Bulls_LineUp)

#remove "DraftedYr" column using the "drop" method
Update_Roster = Bulls_LineUp.drop("DraftedYr",axis="columns")

print("\nUpdated DataFrame")
print(Update_Roster)