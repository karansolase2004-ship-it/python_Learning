a =10 # Global Scope

def display() : 
    a = 15 # Local Scope
    print(a)

display()
# Below print have access to the GLobal a not local a in display function
print(a)

def display1() : 
    # whatever u define in this display1 function would be accessibe in this function only 
    a = 15
    def show() : 
        print(a)
    # show cannot be called outside of display function 
    # because it is local to display function
    show()

# show have access to the a = 15 in display1 function 
display1() 


# in case of condition, for and while loop whatever u write would accessible outside aswell except function
a, b = 5, 6
if a < b : 
    c = a + b
print(c)

for i in range(1, 5) : 
    pass

print(i)
