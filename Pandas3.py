import pandas as pd

#Dataset

data = {
    'Student':["Amit","John","Jacob","David","Steve"],
    'Rank':[1,4,3,5,2],
    'Marks':[95,70,80,60,90]
}

df=pd.DataFrame(data,index=['RowA','RowB','RowC','RowD','RowE'],)

print("Student Record \n \n",df)

# Access rows and columns using integers positions.
print("\n Value = \n",df.iloc[[0,2]])
