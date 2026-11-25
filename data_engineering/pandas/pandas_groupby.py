import pandas as pd

data = {
    "Product": [
        "Laptop", "Phone", "Laptop", "Headphones",
        "Phone", "Keyboard", "Headphones", "Laptop"
    ],
    "Category": [
        "Electronics", "Electronics", "Electronics", "Accessories",
        "Electronics", "Accessories", "Accessories", "Electronics"
    ],
    "Region": [
        "North", "South", "North", "East",
        "South", "East", "North", "South"
    ],
    "Quantity": [2, 5, 3, 8, 4, 10, 6, 1],
    "Unit_Price": [60000, 25000, 60000, 3000, 25000, 2000, 3000, 60000],
    "Rating": [4.5, 4.2, 4.7, 4.0, 4.4, 4.1, 4.3, 4.8]
}

df = pd.DataFrame(data)

print("Original DF")
print(df)
print('Total Quantity: ',df['Quantity'].sum())
print('Mean of Rating: ',df['Rating'].mean())
print('Meadin of Unit_Price: ',df['Unit_Price'].median())
print('Minimum Quantity: ',df['Quantity'].min())
print('Rating Count: ',df['Rating'].count())

print('Price Variance : ',df["Unit_Price"].var())