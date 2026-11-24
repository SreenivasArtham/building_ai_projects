import numpy as np

# Create a large array and save it to a file using memmap
filename = 'large_array.dat'
large_array_shape = (10000, 10000)
dtype = np.float32  # Specify the data type of the array

# Create a memmap object with the desired shape and dtype
large_array = np.memmap(filename, dtype=dtype, mode='w+', shape=large_array_shape)

# Initialize the array with some values (e.g., fill it with random numbers)
rng = np.random.default_rng()
large_array[:] = rng.integers(0, 100, size=large_array_shape, dtype=np.int32)

# Access a small part of the array without loading the entire array into memory
sub_array = large_array[5000:5010, 5000:5010]
print(sub_array)  # Output: A 10x10 array with random float values

# Clean up and ensure that the changes are written to disk
del large_array