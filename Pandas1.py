import pandas as pd

#Dataset

data = {
    'student':["Amit","John","Jacob","David","Steve"],
    'rank':[1,4,3,5,2],
    'marks':[95,70,80,60,90]
}

df=pd.DataFrame(data)

print("Student Record \n \n",df)