# Postional arguement : 

def greet(name, dept) : 
    print(f"Hi {name}")
    print(f"Are you from {dept} department ? ")

greet("Karan", "cs")

# -----------------------------------------------------------

# keyword arguement :
def greet(name, dept) : 
    print(f"Hi {name}")
    print(f"Are you from {dept} department ? ")

# we  used keyword here name and dept 
# no need to aware about order or position about parameter at function definition like as above
greet(dept = "cs", name = "Karan")
name = "mitesh"
# Mixture of positional and keyword arguement :
greet(name, dept='CS')
greet("Mahesh", dept = 'Biology')
# But there should be all positional arguement before keyword arguement Oterwise below will give error : 
# greet(dept = 'CS', name)

# -----------------------------------------------------------------

#Default paremeter you provide at the definition of function : 
# it considered when you don't provide arguement at the call function 
# Passed value at call overirde the default value
def welcome(name = 'XYZ', dept = 'ABC') :
    print(f"Hi {name}, Welcome to our {dept} department !!")

# Calling without passing parameter : 
welcome()
# with parameter : 
welcome(dept = 'Physics', name = 'Kiran')
welcome('Nitin', dept = 'Cultural')

# Please provide non default arguement first and then default at function definition like as below : 
# def count(name, subject, marks, grade='A', attendance = 100, percentage = 100)
# for function count the minimum requirement is to provide parameter matching all non default arguement if you miss any then it will give error 

#----------------------------------------------------------------------

# required positionl arguement :
def Question(name, dept = 'XYZ') :
    print(f"HI {name}, Which {dept} you belong to ?")

# when one of the default arguement is not set at the definition point like name and then if you do not paas the arguement for that parameter at function call then it will give error : Question() missing 1 required positional argument: 'name'
# Question()
# Because parameters becomes compulsory required when default arguement is not set otherwise function call will give error

# --------------------------------------------------------------------

# if you want to write function to sum up the values but do not How much values user will give at function call. SO How to capture it ?
# at the such time arbitrary arguement is used which consist * at its starting 

# arbitaray arguement collects the number into tuple(immutable)
# single Asterisk is used to accept positional arguement 
def sumup(*numbers) : 
    c = 0
    for i in numbers : 
        c += i
    return c

# You can provide the number of arguememnt at whatever length you want
print(f"Sum of numbers is : {sumup(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")
print(f"Sum of numbers is : {sumup(1, 2, 3, 4)}")
