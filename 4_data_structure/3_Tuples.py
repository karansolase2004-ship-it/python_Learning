# Tuples are immutable i.e cannot be changed means you cannot add, remove or change / modify the data

tuple1 = (10, -1, -10, 15, 20)
tuple2 = ("Jenny", "Ram", "Shyam")
tuple3 = (10, "Jenny", True, 10.10)

print(f"1) {tuple1}")
print(f"2) {tuple2}")
print(f"3) {tuple3}")

#if you want to make tuple with one value so put comma after that value
tuple4 = (10,) # pytgon recognize this as the tuple if u put comma there  
tuple5 = (10) # type int not tuple to make it tuple mention it like above 

print(type(tuple4))
print(type(tuple5))

print(f"4) {tuple1[1]}")
print(f"5) {tuple1[-1]}")

# below will give error : 'tuple' object does not support item assignment
# tuple1[0] = -98 

print(f"6) {tuple3[::1]}")
print(f"7) {tuple3[1:4]}") # [1, 4)

print(len(tuple3))

# Nesting tuple : it Creates tuple of tuples

tuple10 = (tuple1, tuple2)
print(f"8) {tuple10}")
tuple11 = (tuple1, tuple3, ("sddas","asdas","sadasd"))

print(f"9) {tuple11}")
print(len(tuple11))

# COncatenation of tuple : It merge the all elements of concatenated tuples into a single tuple

tuple12 = (tuple1 + tuple3)
tuple13 = (tuple1 + ("sddas","asdas","sadasd"))
print(f"10) {tuple12}")
print(f"11) {tuple13}")

print(min(tuple1))
print(max(tuple1))

print(f"12) {tuple12.count(10)}")
print(f"13) {tuple12.index(10)}")

#Below function is used to return index of element in tuple 
print(tuple12.index("Jenny"))

#Converting the list into tuples : 
list1 = [1, 2, 3, 4]
tuple(list1)

# Below and above conversion is temporary 
print(f"15) {tuple(list1)}")
print(type(list1))

tuple15 = (10,) * 5

print(f"16) {tuple15}")