
i = 1
while i <= 5:
   print("What r u doing ? ")
   i += 1

i = 1
while i <= 5 :
   # end is by default = \n in defintion of print that;s print takes new line after printing statement 
   # u can change the end = "" empty i.e internally replcaes \n with ""
   print("Karan", end = "")
   print("Rocks!")
   i += 1 

i = 1
j = 1
while i<=5 :
   print("Karan said", end = "")
   j = 1
   while j<= 5 : 
      print("Hi", end = "")
      j += 1
   i += 1
   print()

data = [2, 'Karan', 23.4, 9, 'Solase', 'Cpp']

i = 0
while i <= 5: 
   print(data[i])
   i += 1

i = 0
n = len(data)

for each in data : 
   if each == 'Karan':
      print("Hi " + each)
      continue
   print(each)

for value in range(10) : 
   print(value)

name = "Karan Solase"
for each in name : 
   print(each)

numbers = [2, 3, 5, -1, 10]

for i in numbers : 
   square = i ** 2
   print("The square is : ", square)