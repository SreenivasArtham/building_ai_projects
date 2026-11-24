import numpy as np

arr = np.array([[10,15,20,25],
                [30,35,40,45],
                [50,55,60,65]
                ])

print(arr)

# select elements greater than 30
arr = arr[arr<50]
print("results :", arr)

# boolean indesing 
arr = np.array([[10,15,20,25],
                [30,35,40,45],
                [50,55,60,65]
                ])

conditions = arr < 50

print("Conditions : ",conditions)

filtered_elements = arr[conditions]

print("Filtered Elements :", filtered_elements)

# row and column indexing 

row_indices = np.array([0,1,2])
col_indices = np.array([1,2,3])
selected_elements = arr[row_indices,col_indices]
print("Selected Elements : ",selected_elements) 

#combine boolean and integer indexes
arr = np.array([[10,15,20,25],
                [30,35,40,45],
                [50,55,60,65]
                ])
combine_condition = (arr > 30) & (row_indices[:, None] < 2)

print("Filtered Selected : ", arr[combine_condition])