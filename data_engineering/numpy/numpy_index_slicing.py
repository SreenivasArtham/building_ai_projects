import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# 1D array indexing same as python lists
print("Element at index 0:", arr[0])  # Output: 10
print("Element at index 2:", arr[2])  # Output: 30  
print("Element at index -1 (last element):", arr[-1])  # Output: 50
print("Element at index -2 (second last element):", arr[-2])  # Output: 40
print("Element at index 1:", arr[1])  # Output: 20
print("Element range from index 1 to 3:", arr[1:4])  # Output: [20 30 40]   
print(" Every other element :", arr[::2])   # Output: [10 30 50]

# 2D array indexing
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(arr_2d)
print("Element at row 0, column 1:", arr_2d[0, 1])  # Output: 2
print("Element at row 2, column 0:", arr_2d[2, 0])  # Output: 7
print("Element at row 1, column 2:", arr_2d[1, 2])  # Output: 6
print("Row 1:", arr_2d[1])  # Output: [4 5 6]
print("Rows 1 to 2:\n", arr_2d[1:])
print("Column 2:", arr_2d[:, 2])  # Output: [3 6 9]
print("Sub-array from row 0 to 1 and column 1 to 2:\n", arr_2d[0:2, 1:3])  # Output: [[2 3] [5 6]]  

#boolean indexing
print("\nBoolean Indexing:")
bool_arr = np.array([1,2,3,4,5,6,7,8,9,10])
# Get elements greater than 5
greater_than_five = bool_arr[bool_arr > 5]
print("Elements greater than 5:", greater_than_five)  # Output: [6 7 8 9 10]
# Get even elements
even_elements = bool_arr[bool_arr % 2 == 0]
print("Even elements:", even_elements)  # Output: [2 4 6 8 10]
# Get elements less than or equal to 3
less_than_equal_three = bool_arr[bool_arr <= 3]
print("Elements less than or equal to 3:", less_than_equal_three)  # Output: [1 2 3]

print("modulus of 3:", bool_arr[bool_arr % 3])

print("modulus of 3:", bool_arr[bool_arr % 3 == 0])  # Output: [3 6 9]


