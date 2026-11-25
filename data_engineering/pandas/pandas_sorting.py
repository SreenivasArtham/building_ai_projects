import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [50, 89, 35, 40],
        'Score': [85, 90, 90, 80]}
df = pd.DataFrame(data)

print("before sorting")
print(df)

print("after sorting")
print(df.sort_values(by='Age'))
print("after sorting descending")
print(df.sort_values(by='Age',ascending=False))
print("after sorting by multiple columns")
print(df.sort_values(by=['Age','Score']))

print("after sorting by quick sort algorithm")
print(df.sort_values(by='Age',kind='quicksort'))

print("after sorting by custom sort")
print(df.sort_values(by='Name',key=lambda col: col.str.lower()))