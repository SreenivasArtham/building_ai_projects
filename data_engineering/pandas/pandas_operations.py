import pandas as pd

df = pd.read_csv("orders.csv")

# accessing columns
print("Columns : ",df.columns)

# accessing rows
print("Rows 5th :", df.iloc[5])
print("Rows 5th and Product column:", df.iloc[5]["Product"])

# accessing head
print("Head :",df.head)

# accessing  AND conditional output
print("Conditional ",df[(df["Category"] == "Electronics") & (df["Country"] == "USA")])

# accessing  OR conditional output
print("Conditional ",df[(df["Category"] == "Electronics") | (df["Country"] == "USA")])

# other conditional

print(">30 ",df[df["Quantity"] > 30])

# in 
print(" in : ",df[df["Country"].isin(['USA','Sweden','Brazil'])])

# modifying the data
df.loc[df["Country"] == "USA", "Country"] = "United States"

# upper
df["Country"] = df["Country"].str.upper()
print("country : ", df["Country"])

# renaming
df.rename(columns={"OrderID": "Order ID"}, inplace=True)
print("renamed Order ID : ",df["Order ID"])

# sortibng
df.sort_values("Price", ascending= False)
print("Ascending Order: ", df["Price"])

# drop 
print(df.drop(38))

# creating new file 

#df.to_csv("new_file.csv",index=False)

# cleaning the data
# df.dropna()
# df.fillna()

#value_counts
print("Value_Counts :",df["Country"].value_counts())

#group by country price sum
print("Group By : ", df.groupby("Country")["Price"].sum())

