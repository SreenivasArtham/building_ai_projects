import numpy as np

arr_1d = np.array([1,2,3,4,5])
arr_2d = np.array([[1,2,3],[3,4,5],[6,7,8]])

print(f"{arr_1d} -> shape: {arr_1d.shape}, mdim: {arr_1d.ndim}")

print(f"{arr_2d} -> shape: {arr_2d.shape}, mdim: {arr_2d.ndim}")

sum = np.sum(arr_1d)
print("sum ", sum)

sum_axis0 = np.sum(arr_1d, axis=0)
print("sum_axis0 ", sum_axis0)

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("Matrix")
print(matrix)
print(matrix.shape)

sum_axis0 = np.sum(matrix,axis=0)
print("sum_axis0", sum_axis0)
print("sum_axis0 shape", sum_axis0.shape)

sum_axis1 = np.sum(matrix,axis=1)
print("sum_axis1", sum_axis1)
print("sum_axis1 shape", sum_axis1.shape)
