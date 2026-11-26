import pandas as pd

chunk_size = 500_000
agg_list = []

for chunk in pd.read_csv(
    'large_data.csv',
    chunksize=chunk_size,
    usecols=['department','salary']
):
    #calculate sum and count per department
    chunk_summary = chunk.groupby('department',observed=True)['salary'].agg(['sum','count'])
    agg_list.append(chunk_summary)

# combine all chunks summary
    
    full_summary = pd.concat(agg_list).groupby('department',observed=True).sum()
    full_summary['avg_salary'] = full_summary['sum'] / full_summary['count']

    print(full_summary) 