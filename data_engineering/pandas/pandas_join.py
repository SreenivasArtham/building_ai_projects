import pandas as pd

data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32]}

data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']}

df1 = pd.DataFrame(data1,index=['K0', 'K1', 'K2', 'K3'])

df2 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])

print(df1, "\n\n", df2)

print("after joioning by default left join")

print(df1.join(df2))

print("after joioning by default outer join")

print(df1.join(df2,how='outer'))