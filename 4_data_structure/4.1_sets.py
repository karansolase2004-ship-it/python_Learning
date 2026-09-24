# Set is immutable like tuple 

set1a = {10, 56, 89, 90, 'jenny', True, 10, 1}
# print(set1[1])

# create empty set if you want to create like that 
set2a = set()
print(type(set2a))

# do not create like empty set like below it is considered as dictionary 
set3a = {}
print(type(set3a))

# Adding element is set : 
set1a.add("vedant")
print(set1a)
# remove throws exception if element is not present in set whereas disacrd does not 
set1a.remove("vedant")
print(set1a)

#discard does not throw exception if element is not present in set 
set1a.discard(10)
print(set1a)

# Pop removes any random item from set and returns it 
print(set1a.pop())
print(set1a)

# you can add tuple aswell in set because they are immutable
set1a.add(("Paresh", 89, 7.8))
print(set1a)

#but you cannot add list in tuple as it is mutable
# set1a.add(['Parekh', 90, 3.4])