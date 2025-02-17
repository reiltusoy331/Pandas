# Pandas adding a new colum using assign() method

import pandas as pd

#Dataset 
Bulls  = {
    'Player':["Kerr","Jordan","Pippen","Rodman","Longley"],
    'Jersey':["25","23","33","91","13",],
    'Drafted Yr':['1988','1983','1987','1981','1990']
}

Bulls_LineUp = pd.DataFrame(Bulls)

# using assign() method that will add a column which at the rightmost portion of the DataFrame
team_roster = Bulls_LineUp.assign(Position = ['PG', 'SG', 'SF', 'PF', 'C'])

# Display the updated DataFrame with new column
print(team_roster) 