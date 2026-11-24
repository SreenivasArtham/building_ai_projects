import numpy as np

arr_int = np.array([1, 2, 3, 4, 5])
print("Array of integers:", arr_int)
print("Data type of the array:", arr_int.dtype)

arr_mixed = np.array([1, 2.5, 3, 4.0, 5])
print("Array with mixed data types (int and float):", arr_mixed)
print("Data type of the array:", arr_mixed.dtype)

#specifying the data type explicitly
arr_float = np.array([1.5, 2.0, 3.0, 4.0, 5.0], dtype=np.float32)
print("Array of floats:", arr_float)
print("Data type of the array:", arr_float.dtype)

arr_float64 = arr_float.astype(np.float64)
print("Array of 64-bit floats:", arr_float64)
print("Data type of the array:", arr_float64.dtype)

arr_bool = np.array([True, False, True, False], dtype=np.bool_)
print("Array of booleans:", arr_bool)
print("Data type of the array:", arr_bool.dtype)

arr_str = np.array(["apple", "banana", "cherry"], dtype=np.str_)
print("Array of strings:", arr_str)
print("Data type of the array:", arr_str.dtype) 

arr_complex = np.array([1 + 2j, 3 + 4j, 5 + 6j], dtype=np.complex128)
print("Array of complex numbers:", arr_complex)
print("Data type of the array:", arr_complex.dtype) 

arr_int32 = np.array([1, 2, 3, 4, 5], dtype=np.int32)
print("Array of 32-bit integers:", arr_int32)
print("Data type of the array:", arr_int32.dtype)