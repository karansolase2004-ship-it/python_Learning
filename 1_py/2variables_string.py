name = input("What is your name ? ")
print(name)

phone_no = 9322521702
name2 = "Mahesh Pathare"
print(phone_no)
print(name2)
print(len(name))

a = 1
b = "Vishwa"

# print(a + b) Cannot concatenate int and string 
# input by default returns the string
a = input("Enter Number of Name : ")
# that why below concatenation is possible even if you input number it will be stored as a string 
print(b + ' ' + a)

print(2 + 3)

# Print char of string name using index
print(name[0])
print(name[1])
print(name[2])
print('name in reverse order : ')
# print char in string in reverse form
print(name[-1])
print(name[-2])
print(name[-3])

# printing substr or str using interval 
print('name in using interval : ')
print(name[1:5])
print(name[0:])
print(name[:4])

print('my' + name[0:])

# Below will give error : 'str' object does not support item assignment because str in python are imutable in terms of range
# name[0:] = 'Karan'

# get address of variable
print(id(a))
print(id(name))

# i and k hold same value 10 so they point to same memory block so the address also would be the same
i = 10
print(id(i))
print(id(10))
k = 10
print(id(k))

# now k pointing to another memory block 
k = 4
print(id(k))

# there is nothing like constant

print('Karan' * 10)

# in below it treats slash as a new character so below line will give an  error
# print('c:\users\karan')
# mention slash like below if you want 
print('c:\\users\\karan')

# Below concatenate
print('karan' 'Solase')

print(name + 'telusko')

text = 'My name is karan,\n welcome to our house'
print(text)