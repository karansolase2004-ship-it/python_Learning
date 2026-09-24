set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Akash'}
set3 = {'Ankur', 'Pradeep', 'Ram'}

# it will return element which are set1 but not in set2
print(set1 - set2)
print(set1.difference(set2))
print(set1.difference( ('Shyam',) ))

# first perform set1 - set2 = {'Ram', 'Shyam'} - set3 = {'Shyam'}
print(set1.difference(set2, set3))

# difference update : whatever result comes of differnce that is newly assigned to set1
# set1 = set1-set2 = {'Shyam', 'Ram'}
print(set1.difference_update(set2))
print(set1)

set1 = {'Ram', 'Shyam', 'Jenny'}

# symmetric difference return all the objects that are either in set1 or set2 but not in both 
# Jenny is in both so it is not returned 
print(set1.symmetric_difference(set2))

# Symmteric difference not allowed on multiple set but below operator of symmetric differnece can be applied on multiple set 
print(set1 ^ set2 ^ set3)

set4 = set1 ^ set2 ^ set3 
print(set4)

# Rather than new set such as set4 if you want assign values to exisiting set such as set1 then call below function : 
# set1.symmteric_difference(set2, set3)

# two sets which do not anything common in them called disjoint of each other 
set5 = {1, 2}
set6 = {"Mahesh", "Karan"}
print(set5.isdisjoint(set6))

print(set1.isdisjoint(set2))

set7 = {1}
set8 = {1, 2}
print(set7.issubset(set8))
print(set8.issubset(set7))

print(set8.issubset((1, 2)))
print(set8.issubset([1, 2]))

# Set a is superset of b if every element of that belongs to set b also belongs to set A
# set8 is superset of set7 because every element in set7 belongs to set8 
# if a is subset of b then b is superset of s
print(set8.issuperset(set7))

# delete all elements in set8
set8.clear()
print(set8)

# delete set8
del set8
# print(set8)