# value in dictionaries are mutable where key is immutable
# Last value would be assigned if duplicate exist like 'Ram'
phone_no = {
    'Ram' : 1234, 
    'Shyam' : 3456, 
    'Mohan' : 1111,
    'Ram' : 6789}
print(phone_no)

# key is case sensitive 
print(phone_no['Shyam'])

#Another method to create dictionaries :
phone_no = dict({
    'Ram' : 1234, 
    'Shyam' : 3456, 
    'Mohan' : 1111,
    'Ram' : 6789
})
print(phone_no)
phone_no = dict([('Ram',1234), ('Shyam', 3456), ('Mohan',1111), ('Ram', 6789)])
print(phone_no)

# Mutating value 
phone_no['Mohan'] = 99990
print(phone_no)

# Adding the items : 
phone_no['Madhav'] = {1111, 2222, 3333}
print(phone_no)

print(type(phone_no['Madhav']))

phone_no['Shyam'] = {'Shyam_home' : 5555, 'Shyam_work' : 4444}
print(phone_no)

print(phone_no['Shyam'])

print(phone_no.get('Ram'))

data = {
    1 : 'jenny',
    2 : 'Ram',
    0 : 'Mohan'
}

# Deleting the particular key : 
# del phone_no['Ram']

# pop delete the value and also written it 
print(phone_no.pop('Shyam'))
print(phone_no)

# Delete the all element in dictionary
# phone_no.clear()
# print(phone_no)

# Used to display all keys
print(phone_no.keys())

# Used to display all values 
print(phone_no.values())

for i in phone_no.items():
    print(i)


# Copying elements : 
phone_no2 = phone_no.copy()
print(phone_no2)

print(len(phone_no))