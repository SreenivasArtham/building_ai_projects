import numpy as np
import pandas as pd

df = pd.DataFrame({'FirstName': ['Vipul', 'Ashish', 'Milan'],
                            "Gender": ["", "", ""],
                            "Age": [0, 0, 0]})
df['Department'] = np.nan

print(df)
print(df.dropna(how='all', axis=1, inplace=True))
print(df)

df = pd.DataFrame({'FirstName': ['Vipul', 'Ashish', 'Milan'],
                            "Gender": ["", "", ""],
                            "Age": [0, 0, 0]})

df['Department'] = np.nan
print(df)

nan_value = float("NaN")
df.replace("", nan_value, inplace=True)
print(df)
df.dropna(how='all', axis=1, inplace=True)

print(df)