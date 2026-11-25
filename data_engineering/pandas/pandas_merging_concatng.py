import pandas as pd

data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
         'Age': [17, 14, 12, 52],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

df1 = pd.DataFrame(data1, index=[0, 1, 2, 3])

df2 = pd.DataFrame(data2, index=[4, 5, 6, 7])

print(df1, "\n\n", df2)

frames = [df1, df2]
concat_result = pd.concat(frames)
print(concat_result)

df1 = pd.DataFrame(data1, index=[0, 1, 2, 3])

df2 = pd.DataFrame(data2, index=[2, 3, 6, 7])

print(df1, "\n\n", df2)

concat_result2 = pd.concat([df1,df2], axis=1,join='inner')

print("concat axis =1 :",concat_result2)

res2 = pd.concat([df1, df2], axis=1, sort=False)

print(res2)

data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
        'Mobile No': [97, 91, 58, 76]} 

data2 = {'Name':['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'], 
        'Age':[22, 32, 12, 52], 
        'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons'],
        'Salary':[1000, 2000, 3000, 4000]} 
  
df1 = pd.DataFrame(data1,index=[0, 1, 2, 3])
  
df2 = pd.DataFrame(data2, index=[2, 3, 6, 7]) 

print("Ignore Index: ", pd.concat([df1, df2], ignore_index=True))