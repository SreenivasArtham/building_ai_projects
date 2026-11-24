import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

print("Array a:", a)
print("Array b:", b)

# Element-wise operations
print("\nElement-wise addition:", a + b)  # Output: [ 7  9 11 13 15]
print("Element-wise subtraction:", a - b)  # Output: [-5 -5 -5 -5 -5]
print("Element-wise multiplication:", a * b)  # Output: [ 6 14 24 36 50]
print("Element-wise division:", b/a)  # Output: [0.16666667 0.28571429 0.375 0.44444444 0.5]
print("Element-wise power:", a ** 2)  # Output: [ 1  4  9 16 25]
print("Element-wise square root:", np.sqrt(a))  # Output: [1.         1.41421356 1.73205081 2.         2.23606798]

#scalar operations
print("\nScalar addition:", a + 10)  # Output: [11 12 13 14 15]
print("Scalar multiplication:", a * 2)  # Output: [ 2  4  6  8 10]
print("Scalar division:", a / 2)  # Output: [0.5 1.  1.5 2.  2.5]
print("Scalar power:", a ** 3)  # Output: [ 1  8 27 64 125] 
print("Scalar square root:", np.sqrt(a))  # Output: [1.         1.41421356 1.73205081 2.         2.23606798]

#Comparison operations
print("\nComparison operations:")
print("a > 3:", a > 3)  # Output: [False False False  True  True]
print("a < 3:", a < 3)  # Output: [ True  True False False False]
print("a == 3:", a == 3) 