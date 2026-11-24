import numpy as np

matrix_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Matrix:")
print(matrix_2d)
print("Shape of 2D Matrix:", matrix_2d.shape)
print("Number of dimensions:", matrix_2d.ndim)
print("Size of 2D Matrix:", matrix_2d.size)
print("Data type of elements:", matrix_2d.dtype)


#3D Matrix
matrix_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Matrix:")
print(matrix_3d)
print("Shape of 3D Matrix:", matrix_3d.shape)
print("Number of dimensions:", matrix_3d.ndim)
print("Size of 3D Matrix:", matrix_3d.size)
print("Data type of elements:", matrix_3d.dtype)

#creating a multi-dimensional array with specified shape
multi_dim_array = np.zeros((3, 4))  # 3 rows, 4 columns
print("\nMulti-dimensional array with specified shape (3, 4):")
print(multi_dim_array)
print("Shape of multi-dimensional array:", multi_dim_array.shape)

#creating a multi-dimensional array with specified values
ones_3d_array = np.ones((2, 3, 4))  # 2 blocks, 3 rows, 4 columns
print("\n3D array filled with ones (2, 3, 4):")
print(ones_3d_array)
print("Shape of 3D array:", ones_3d_array.shape)
