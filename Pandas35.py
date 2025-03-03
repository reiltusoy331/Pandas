# Pandas adding column to a DataFrame using assign() method

import pandas as pd

#Dataset 
Bulls  = {
    'Player':["Kerr","Jordan","Pippen","Rodman","Longley"],
    'Jersey':["25","23","33","91","13",]    
}

#DataFrame
Bulls_LineUp = pd.DataFrame(Bulls)

#Start the index to 1
Bulls_LineUp.index=range(1,len(Bulls_LineUp)+1)


print("The Bulls Roster \n",Bulls_LineUp)

#add a new column using the assign method which will be added on the rightmost column
Update_Roster = Bulls_LineUp.assign(DraftedYr=['1988','1983','1987','1981','1990'])

print("\nUpdated DataFrame with additional column")
print(Update_Roster)