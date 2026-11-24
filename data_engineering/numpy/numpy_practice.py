import numpy as np
import time

python_list = [1, 2, 3, 4, 5]

numpy_array = np.array([1, 2, 3, 4, 5])

print("Python List:", python_list)
print("NumPy Array:", numpy_array)

print("Type of Python List:", type(python_list))
print("Type of NumPy Array:", type(numpy_array))

print("increasing each element of the Python list by 5:", [x + 5 for x in python_list])
print("increasing each element of the NumPy array by 5:", numpy_array + 5)

size = 10000000
python_list_large = list(range(size))
numpy_array_large = np.arange(size)

print("Time taken to increase each element of the large Python list by 5:")


start_time = time.time()
result_python = [x + 5 for x in python_list_large]
time_python_list = time.time() - start_time
print("Time taken for Python list:", time_python_list, "seconds")

start_time = time.time()
result_numpy = numpy_array_large + 5
time_numpy_array = time.time() - start_time
print("Time taken for NumPy array:", time_numpy_array, "seconds")

print("How many times faster is NumPy compared to Python list:", time_python_list / time_numpy_array)