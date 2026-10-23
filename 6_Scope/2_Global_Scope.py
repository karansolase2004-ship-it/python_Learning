# we know we can access the global variable anywhere in the code but what if we try to modify it in function definiton
a = 10 

def display() : 
    # below line of a modification will give error : 
    # (cannot access local variable 'a' where it is not associated with a value)
    # a = a + 1
    print(a)

display() 
# but if there is need to modify the global variable :
# then you can declare the same global variable using keyword global and modify it 

def display1() : 
    # Now below variable a belongs to the global variable a 
    global a 
    a = a + 1
    print(a)

display1()

# b = 10

def display2() : 
    b = 20
    def show() : 
        global b
        b = 13
        # Now below assignment statement will give error because globally accessed b have been commented. so b is not defined 
        # b = b + 1
        # it means that whenever you declare variable with global keyword then it compulsory belongs to that globally declared variable even after existing local variable of same name
        print(b)
    show()
    # THis below b will print 20 because b being global is just up to show function 
    print(b)

display2()
print(b)

x: str = 1