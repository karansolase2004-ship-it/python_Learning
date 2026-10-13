name = 'Krishna'
age = 40
height = 1.6

# using COncatenation :
# print("My Name is" + name, "I am" + age, "years old")
# Above will give error : can only concatenate str (not "int") to str

print("My Name is : "+name, "i am" + str(age), "years olds")

# so  while priinting any statement we will have variables from different datatypes 
# for that we will use fstring : 

print(f"My name is {name}.\n I am {age} old with height {height}cm")
print(f"i am krishna father with age {age * 2} with {height*2}cm")