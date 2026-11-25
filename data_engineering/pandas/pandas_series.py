import pandas as pd
import numpy as np

data = np.array(['g','e','s','k','t'])
s = pd.Series(data)
print("Pandas Series : ",s)

df = pd.DataFrame()
print(df)

df = pd.DataFrame(data)
print("DataFrame : ",df)

data = { 'A': np.array([1, 4, 7]),
         'B': np.array([2, 5, 8]),
         'C': np.array([3, 6, 9]) }
df = pd.DataFrame(data)
print(df)

data = [
    {'name': 'Mike', 'degree': 'MBA', 'score': 90},
    {'name': 'Dan', 'degree': 'BCA', 'score': 40},
    {'name': 'Emilia', 'degree': 'M.Tech', 'score': 80},
]
df = pd.DataFrame(data)
print(df)

#accessing index

print("Accessing Index :", df.index)

# Access the first three rows and the 'Name' and 'Age' columns
subset = df.loc[0:2, ['name', 'degree']]
print(subset)

# Access the 'Salary' of the row with label 2
score_at_index_2 = df.at[2, 'score']
print(score_at_index_2)


player_list = [['M.S.Dhoni', 36, 75, 5428000],
               ['A.B.D Villers', 38, 74, 3428000],
               ['V.Kohli', 31, 70, 8428000],
               ['S.Smith', 34, 80, 4428000],
               ['C.Gayle', 40, 100, 4528000],
               ['J.Root', 33, 72, 7028000],
               ['K.Peterson', 42, 85, 2528000]]

df = pd.DataFrame(player_list, columns=['Name', 'Age', 'Weight', 'Salary'])
print(df) 

# slicing integer based index
df1 = df.iloc[0:4]
print("Slicing Integer Index : ",df1)

# slicing columns

df2 = df.iloc[:,0:2]
print(df2)