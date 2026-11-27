def greet(name):
    print('Hello ',(name))

greet('Sreeni')
greet('Mayank')

# lamda function anynoumos function
add = lambda x,y: x+y
print(add(5,6))

square = lambda x : x*x
print(square(10))

# filter
numbers = [2,3,5,6,7,8,9,11,12]
even_numbers = list(filter(lambda x : x%2 == 0,numbers))
print(even_numbers)

square_numbers = list(map(lambda x : x*x ,numbers))
print(square_numbers)

print(list(map(lambda x : (x*5/100),numbers)))

# reccursion

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
print('Factorial :', factorial(6))