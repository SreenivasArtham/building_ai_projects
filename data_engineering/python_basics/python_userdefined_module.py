import python_modular as pm

data = [1,2,3,4,5,6]
evens = pm.filter_even(data)

print('Original Data ',data)
print('Evens ',evens)
print('Square: ',pm.square(5))

square_list = [pm.square(x) for x in data]
print(square_list)