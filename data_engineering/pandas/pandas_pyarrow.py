import pandas as pd

for chunk in pd.read_csv(
    'large_data.csv',
    chunksize=500_000,
    engine='pyarrow',
    dtype_backend='pyarrow'
)
    # Procees chunk  makes pandas read CSVs multi-threaded and store strings using far less RAM:
    pass