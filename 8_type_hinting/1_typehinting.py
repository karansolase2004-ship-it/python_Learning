#type hinting is the way of telling to what kind of datatype the variable belongs because 
# Without type hints, if you accidentally pass a text string into a function meant for calculations, Python won’t notice until that exact line of code executes, causing a runtime crash.By adding type hints and using a tool like mypy, you can scan your code for mistakes instantly.
#In large projects, you often have to use functions written by other people (or by you, six months ago). Without type hints, you have to guess what the function needs.


# that str is type hinting
x: str = 1
# we have installed static code analysis tool named mypy
# After writing above code and running below command it will show the error which is not shown after running the code normally by ctrl + r
""" 
python -m mypy D:\Python\8_type_hinting
 """

# variable a, b, and c have type int and this -> int show that return in None that is type hinting
def add_numbers2(a: int, b: int , c: int) -> None: 
    print(a + b + c)

add_numbers2("Karan", "Anil", "Solase")

# above function will called and print the values but we r expected to give integer value their This thing will be shown by static analysis tool by running the command given in triple Quote


# [[1, 2, 3], [], []]
# type for above data is list[list[int]]

# list[list[int]] is type hinting 
a: list[list[int]] = [[1, 2], [3, 4]]
b : dict[str, str] = {'a': 'b'}
c : set[str] = {"a", "b"} 

# wherever we use vector it will be replaced by list[float] 
vector = list[float]

# tool will also give because we mentioned return type vector but havenot returned it 
def foo(v : vector) -> vector : 
    print(v)

foo([3.4, 6.5, 8.9, 0.2, 2.3])

# tool will give error for below : 
# foor(3.4, 6.5, 8.9, 0.2, 2.3) because passed arguement is not list


# video stopped watching at 12:56 
