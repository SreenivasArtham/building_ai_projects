# Opening and closing a file
file = open('test.txt','r')
content = file.read()
print(content)
file.close()

# Write
file = open('new_file.txt','w')
file.write('Hello To Python World 1')
file.close()

# append
file = open('new_file.txt','a')
file.write('\n New Line')
file.close()

# Read & Write 
file = open('test.txt','r+')
content = file.read()
print('Before Writing',content)
file.write('\nAdding new content on this file')
file.close()
