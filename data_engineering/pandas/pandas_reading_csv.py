import pandas as pd

df = pd.read_csv('orders.csv')

print(df)

print('read csv using specific columns')
print(pd.read_csv('orders.csv',usecols=['OrderID','CustomerName']))

print('read csv using setting index column')
print(pd.read_csv('orders.csv', index_col='OrderID'))

print('read csv using setting Missing Values')
print(pd.read_csv('orders.csv', na_values=['N/A','NaN']))


print('read csv using setting nrows ')
print(pd.read_csv('orders.csv', nrows=3))

print('read csv using setting skiprows ')
print(pd.read_csv('orders.csv', skiprows=[4,6]))

print('DataFrame to Json')
print(df.to_json('file.json',orient='split',compression='infer',index=True))

print('Read from JSON')
print(pd.read_json('file.json',orient='split',compression='infer'))