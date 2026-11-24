import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print("Array : ", arr)

# Basic statistics

print(f"Sum : {np.sum(arr)}")
print(f"Mean: {np.mean(arr)}")
print(f"Median: {np.median(arr)}")
print(f"Standard deviation: {np.std(arr)}")
print(f"Variance : {np.var(arr)}")
print(f"Min : {np.min(arr)}")
print(f"Max: {np.max(arr)}")
print(f"index of Min : {np.argmin(arr)}")
print(f"index of Max : {np.argmax(arr)}")

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("2D Array : ",matrix)
print(f"sum of all elem,ents : {np.sum(matrix)}")
print(f"sum of rows  axis = 0: {np.sum(matrix, axis=0)}")
print(f"sum of rows axis = 1: {np.sum(matrix, axis=1)}")
print(f"sum of rows  axis = 0: {np.mean(matrix, axis=0)}")
print(f"sum of rows axis = 1: {np.mean(matrix, axis=1)}")
