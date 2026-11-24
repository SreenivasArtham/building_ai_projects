import numpy as np

arr = np.arange(45) 
print("Original Array:",arr)

# Reshape - changes view and does not copy data
reshaped = arr.reshape(3,15)
print(reshaped)

flattened = reshaped.flatten()
print("flattened :", flattened)

autoreshape = arr.reshape(3,-1) # -1 auto calculate
print("auto reshape :", autoreshape)

#Transpose

matrix = np.array([[1,2,3],[4,5,6]])
print("Original array", matrix)
print("Transposed ", matrix.T)

#concatination

print("concatination")
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print("orginal")
print(a)
print(b)

print("vertical concatination")
print(np.vstack((a,b)))

print("horizantal concatination")
print(np.hstack((a,b)))

print(np.concatenate((a,b), axis=0)) #vertical
print(np.concatenate((a,b), axis=1)) #horizental



