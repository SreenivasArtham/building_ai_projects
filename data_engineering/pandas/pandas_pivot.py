import pandas as pd

# creating dataframe
df = pd.DataFrame({'Product': ['Carrots', 'Broccoli', 'Banana', 'Banana',
                               'Beans', 'Orange', 'Broccoli', 'Banana'],
                   'Category': ['Vegetable', 'Vegetable', 'Fruit', 'Fruit',
                                'Vegetable', 'Fruit', 'Vegetable', 'Fruit'],
                   'Quantity': [8, 5, 3, 4, 5, 9, 11, 8],
                   'Amount': [270, 239, 617, 384, 626, 610, 62, 90]})

print(df)

# Get the Total Sales of Each Product

print("Get the Total Sales of Each Product")
print(df.pivot_table(index=['Product'],values=['Amount'],aggfunc='sum'))
print("Get the Total Sales of Each Category")
print(df.pivot_table(index=['Category'],values=['Amount'],aggfunc='sum'))

print("Get the Total Quantity of Each Category")
print(df.pivot_table(index=['Category'],values=['Quantity'],aggfunc='sum'))

print("Get the Mean, Median, Minimum Sale by Category")
print(df.pivot_table(index=['Category'], values=['Amount'],aggfunc={'median', 'mean', 'min'}))

print("Get the Mean, Median, Minimum Sale by Product")
print(df.pivot_table(index=['Product'], values=['Amount'],aggfunc={'median', 'mean', 'min'}))