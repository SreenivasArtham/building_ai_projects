import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Alice", "David"],
    "Age": [25, 30, 25, 40],
    "City": ["NY", "LA", "NY", "Chicago"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("Modified DataFrame (no duplicates)")
print(df.drop_duplicates())

print("Remove Duplicates by column name")
print(df.drop_duplicates(subset=['Name']))

print("Remove Duplicates and keep last occurance ")
print(df.drop_duplicates(keep='last'))

print("Remove ALL Duplicates ")
print(df.drop_duplicates(keep=False))