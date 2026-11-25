import pandas as pd

data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age':[27, 24, 22, 32]}

data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print("df1 :")
print(df1)
print("df2 :")
print(df2)
print("After Merging")
print(pd.merge(df1,df2,on='key'))


data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K1', 'K0', 'K1'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],}

data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K0', 'K0', 'K0'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}

df1 = pd.DataFrame(data1)

df2 = pd.DataFrame(data2)

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print("df1 :")
print(df1)
print("df2 :")
print(df2)
print("After Merging with multiple Keys")
print(pd.merge(df1,df2,on=['key','key1']))

print("After Merging with Left JOIN")
print(pd.merge(df1,df2,how='left',on=['key','key1']))

print("After Merging with Right JOIN")
print(pd.merge(df1,df2,how='right',on=['key','key1']))

print("After Merging with OUTER JOIN")
print(pd.merge(df1,df2,how='outer',on=['key','key1']))

print("After Merging with inner JOIN")
print(pd.merge(df1,df2,how='inner',on=['key','key1']))