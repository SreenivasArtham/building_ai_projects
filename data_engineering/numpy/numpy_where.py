import numpy as np

arr = np.array([10,-5,20,-3,0])
print("Original Array :",arr)
#modify array in place
arr[arr<0] = 0
print(arr)

# faster way
arr = np.array([10,-5,20,-3,0])
np.putmask(arr,arr<0,0)
print("putMask :", arr)

#where condition with new array creation
arr = np.array([10,-5,20,-3,0])
results = np.where(arr<0,0,arr)
print("Array :",arr)
print("Results :",results)

arr = np.array([80,75,40,90,20])
grades = np.where(arr>75,'Good','Ok')
print("Array :",arr)
print("Grades :",grades)