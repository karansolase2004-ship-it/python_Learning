# tuples and list allows duplicate while sets have unique elements 
# sets are unordered due to which indexing is not allowed
# so u cannnot perform operation related to index 

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 10, 11}
set3 = {8, 6, 4, 5, 12}

set4 = {"Karan", "Mahesh", "Swayam"}
set5 = {"Ratan", "Mahesh", "Swayam"}

print(set1.union(set2, set3))
# union using operator. but using below operator u can pass only set as arguement :
print(f"1. {set1 | set2 | set3}") 

# whereas using union u can pass tuple and list :
print(set1.union((9, 0, 23,21,54,556), [2323,423434,234234,42343244]))

print(set1.intersection(set2))

# update perform union and also update set4
set4.update(set5)
print(set4)

# u can give tuple and list as an parameter for update
set5.update(('jignesh', 'Vasant', 'Mitesh'), ['ROhan', 'Kartik', 'Ravi'])
print(set5)

print(set1.intersection(set2, set3))
print(set1)

# tuple with single element should always be with comma 
print(set1.intersection([4], (4,)))
# 0 is not common so below will give empty set()
print(set1.intersection([0], (0,)))

# Intersection update : whatever come as an intersection result is unioned with caller set
set6 = {"Karan", "Mahesh"}
set6.intersection_update(("Karan",))
print(set6)