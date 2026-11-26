import pandas as pd

import pandas as pd

df = pd.DataFrame({
    "employee": ["Alice", "Bob", "Charlie", "Diana"],
    "department": ["Sales", "Sales", "IT", "IT"],
    "salary": [60000, 80000, 100000, 120000]
})

print('Original Data Frame')
print(df)

print('GroupBy')
print(df.groupby('department')['salary'].agg('mean'))

print('in order to transform this to original df')
print(df.groupby('department')['salary'].transform('mean'))

df['dept_avg_mean'] = df.groupby('department')['salary'].transform('mean')

print(df)

