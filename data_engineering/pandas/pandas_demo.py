import pandas as pd
# Load from CSV
df = pd.read_csv("orders.csv")
print(df)
# from json /dictonary
data ={
    'Name':['Sreeni', 'Siddu', 'Smart'],
    'Age':[43,25,34],
    'Country':['USA', 'Uk','IN']
}
df = pd.DataFrame(data)
print("Df : ",df)


