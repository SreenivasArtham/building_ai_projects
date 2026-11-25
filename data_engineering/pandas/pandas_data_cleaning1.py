import pandas as pd
import numpy as np

data = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}
df = pd.DataFrame(data)

print('Original data frame')
print(df)

missingvalue = df.isnull()
print(missingvalue)

nonmissing = pd.notnull(df['Third Score'])
print('nonmissing by Third Score')
print(df[nonmissing])

print('filling missing values with zero')
print(df.fillna(0))

print('filling missing values with previous value(Forwardfill)')
print(df.ffill())

print('filling missing values with previous value(Backwardfill)')
print(df.bfill())