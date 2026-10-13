 # Range function syntax : range(start, stop, step_size)
#  BY Default step size is 1
# step size allows us move forward 

# in below stop is 5, start is 0, step size = 1
# range is [0, 5)
for each in range(5) : 
    print(each, end = "")

# Below print next line
print()

# stop = 5, start = 2,  step size = 1
# range is [2, 5)
# 2 (jump 1 step from 2) => 3
# 3 (jump 1 step from 3) => 4
# 4 (jump 1 step from 4) => 5 out of bound.
for each in range(2, 5):
    print(each, end="")

print()

# start = 2, stop = 6, step - size = 2
# range [2, 6)
# 2 (jump 2 step from 2) => 4
# 4 (jump 2 step from 4) => 6 out of bound
for each in range(2, 6, 2) :
    print(each, end = "")

print()

a = range(2, 5)
print(type(a))
print(a[0])
print(a[1])
print(a[2])
# print(a[3])index is out of range

for i in a : 
    print(i, end = "")

print()

# Reverse order : 
# 10 pasun 0 paryant Maghe yet aahot mhnun -1 (going towards left)
for i in range(10, 0, -1) : 
    print(i, end = " ")

print()

# -1 pasun -10 paryant Maghe yet aahot mhnun -1 : (going towards left)
for i in range(-1, -10, -1) :
    print(i, end = " ")

print()

total = 0
# sum of numbers from 1 to 100
for i in range(1, 101) : 
    total += i
print(total)