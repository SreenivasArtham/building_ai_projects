import numpy as np

arr_3d = np.array([
[
  [1,2,3],
  [4,5,6]  
],
[
    [7,8,9],
    [10,11,12]
]
])

print("3D Array")
print(arr_3d)
print(f"Shape : {arr_3d.shape} (depth=2, rows=2, columns=3)")

sum_axis0 = np.sum(arr_3d,axis=0)
print(sum_axis0)
print(f"Shape: {sum_axis0.shape}")

sum_axis1 = np.sum(arr_3d,axis=1)
print(sum_axis1)
print(f"Shape: {sum_axis1.shape}")

sum_axis2 = np.sum(arr_3d,axis=2)
print(sum_axis2)
print(f"Shape: {sum_axis2.shape}")