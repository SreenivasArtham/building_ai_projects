import numpy as np

arr1 = np.array([1, 2, 3, 4, 5,True, False, "Hello", 3.14])
print("Array with mixed data types:", arr1)
print("Data type of the array:", arr1.dtype)

# better to have all similar data types in a NumPy array for performance and memory efficiency
# as it is designed to work with homogeneous data types. If you need to store mixed data types, consider using a structured array or a pandas DataFrame instead.
#otherwise, NumPy will upcast the data types to a common type, which may lead to unexpected behavior or loss of precision.

arr2 = np.array([1, 2, 3, 4, 5])
print("Array with similar data types:", arr2)
print("Data type of the array:", arr2.dtype)

arr3 =np.arange(10)
print("Array created using arange:", arr3)

arr4 = np.arange(0, 10, 2)
print("Array created using arange with step size:", arr4)

arr5 = np.linspace(1, 100, 10)
print("Array created using linspace:", arr5)

arr6 = np.zeros(5)
print("Array created using zeros:", arr6)

arr7 = np.zeros((2, 3))
print("2D Array created using zeros:", arr7)

arr8 = np.ones(5)
print("Array created using ones:", arr8)

arr9 = np.ones((2, 3))      
print("2D Array created using ones:", arr9) 

arr10 = np.full(5, 7)
print("Array created using full:", arr10)

arr11 = np.eye(5)
print("Identity matrix created using eye:", arr11)

arr12 = np.random.rand(5)
print("Array created using random.rand:", arr12)

arr13 = np.random.randint(1, 10, size=5)
print("Array created using random.randint:", arr13)

