# Pandas deleting a colum using drop() method

import pandas as pd

#Dataset 
Bulls  = {
    'Player':["Kerr","Jordan","Pippen","Rodman","Longley"],
    'Jersey':["25","23","33","91","13",],
    'Drafted Yr':['1988','1983','1987','1981','1990']
}

Bulls_LineUp = pd.DataFrame(Bulls)

print("Bulls Roster\n",Bulls_LineUp)

# Drop a column
team_roster = Bulls_LineUp.drop("Drafted Yr",axis='columns')

# Display the updated DataFrame
print("\n","Bulls Roster(Updated)\n",team_roster) 