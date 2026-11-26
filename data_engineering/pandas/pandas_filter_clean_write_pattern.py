import pandas as pd

input_file = 'large_data.csv'
output_file = 'filtered_output.csv'
chunk_size = 500_0000 # 500K rows per batch

#dtypes

dtypes = {
    'employee_id':'int32',
    'department':'category',
    'salary':'float32'
}

first_chunk = True;

for chunk in pd.read_csv(
    input_file,
    chunksize=chunk_size,
    usecols=list(dtypes.keys()),
    dtype=dtypes
):
    # filter and transformations
    processed = chunk[chunk['salary'] > 100_000].copy()
    processed['bonus'] = processed['salary'] * 0.10

    #append directly to disk

    processed.to_csv(
        output_file,
        mode='w' if first_chunk else 'a',
        header=first_chunk,
        index=False
    )
    first_chunk=False

