# Pandas adding a new colum using insert() method

import pandas as pd

#Dataset 
Bulls  = {
    'Player':["Kerr","Jordan","Pippen","Rodman","Longley"],
    'Jersey':["25","23","33","91","13",],
    'Drafted Yr':['1988','1983','1987','1981','1990']
}

result = pd.DataFrame(Bulls)

# Insert a new column at index 2 (i.e. after 'Jersey') with the values
result.insert(2, "Position", ['PG', 'SG', 'SF', 'PF', 'C'])

print(result) 