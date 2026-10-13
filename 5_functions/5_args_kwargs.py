# *args : arbitrary positional arguements
# *numbers == *args (u cann put whatever u want )
# *args collect all arguements in tuple which make them immutable 
def sumup(*numbers) : 
    c = 0
    # below will give error 
    # numbers[0] = 4
    for i in numbers : 
        c += i
    print(f"Sum is {c}")

sumup(23,234, 324,89,56532)
sumup(12,46,989,6,45,434,3,23)

# # # # # # # # # # # # 

def add(*numbers, name) : 
    print(f"numbers : {numbers} and name : {name}")

# numbers will consider (1, 2, "Karan") as tuple for below call which is not as expected we want karan to go to name 
# add(1, 2, "Karan")
# for that we can call place call like below : 
add(1, 2, name = "Karan")
# but what if we want arguement *numbers as (1, 2, 3) and a = 10; 
# for that we need to change the function definition like below : 
def add2(a, *numbers) : 
    print(f"numbers : {numbers} and a : {a}")

add2(10, 1, 2, 3)

# Note : Write the normal arguement first and then arbitrary positional arguement and arbitrary keyword arguement.

# **kwargs : arbitrary keyword arguement 
# here we pass arguement with their parameters such as name = "karan", dept = "Cs" so we can say it as a key and value form.

# **info ==  **kwargs
def info_person(**info) : 
    # u can use i, j instead of key, value
    for key, value in info.items():
        print(key, value) 
    # here it print key n value both
    for i in info.items() : 
        print(i)

info_person(name="Ram", age=30, height=3.4)
info_person(Teacher="Yadav mam", Subject="LLM", Credit=4)

# below syntax is invalid : 
""" def info_person2(**info, *args) : 
    print(f"info : {info}, other : {args}") """

# as per the given note above u cannot pass arbitrary keyword arguement before arbitrary positional arguement which makes above function syntax invalid. So *args should be before **kwargs

def info_person2(name1, age, rollno, *args, **info) : 
    print(f"name : {name1}, rollno: {rollno}, age : {age}, args = {args}, kwargs = {info}")

info_person2('Karan', 32, 90, 1, 2, 3, 4, name='karan', msg='Hello', que='How r u ? ')