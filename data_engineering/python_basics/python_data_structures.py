word = 'Pyhton'

print(word[5])
print(word[-1])
print('Reverse String :',word[::-1])
print('first 3 characters:',word[0:3])
print('first 3 characters:',word[:3])
print('alternative chatacters:',word[::2])
print('alternative chatacters 2 :',word[::3])

# Lists

marks = [50,60,89,90]
print(marks)
print(type(marks))
print('First Element:',marks[0])
print('Last Element:',marks[-1])
print('first three items:',marks[:3])
print('after concatination :',marks + [85,95,100])

#List Operations

print('appendijng :',marks.append(100))
print('poping last element: ',marks.pop())
print('poping first element: ',marks.pop(0))
marks[0:1] = [60,30]
print('after replace: ',marks)
marks[0:2] = []
print('after delete: ',marks)
marks[:] = []
print('Empty List : ',marks)
print('Length List : ',len(marks))
new_list = ['a','b','c',['d','e','f']]
print('Accessing sublist ',new_list[3][0])
new_list = ['a','d','b','c']
new_list.reverse()
print('Reverse :', new_list)
new_list.sort()
print('Sorted :', new_list)

# Sets unordered collection of distinction

marks = {34,56,12,34}
print('Marks Set :',marks) # remove duplicates
print(type(marks))
marks.add(50) # mutable datatype
print(marks)
marks.remove(12)
print(marks)

# Union Intersection and Difference
a = {1,2,3}
b = {3,4,5}
print('Union ',a|b)
print('Intersection ',a&b)
print('Difference ',a-b)
print('3 in a ', 3 in a)

# remove duplicates
list = {1,2,2,3,3,4,4,5}
unique_values = set(list)
print(unique_values)


