employees = ['john','sreeni','ashish']
for emp in employees:
    print(emp)

for index in range(len(employees)):
    print(index)
    print(employees[index])

for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(1,11):
    if i==5:
      continue
    print(i)

for i in range(1,11):
    if i==5:
      pass # placeholder only
    print(i)

num = int(input('Enter a Number'))
for i in range(2,num):
    if num%i == 0:
        print('not a prime')
        break

x = 0

while x<5:
    print(x)
    x +=1

