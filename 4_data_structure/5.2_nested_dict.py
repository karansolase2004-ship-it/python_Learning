student_data = {
    'Ram' : {'Rollno' : 10, 'age' : 20, 'course' : 'Python'},
    'Mohan' : {'Rollno' : 20, 'age' : 22, 'course' : 'Java'}
}

# Printing particular data
print(student_data['Mohan'])
print(student_data['Mohan']['Rollno'])

# Adding the key and value : 
student_data['Mohan']['phone_no'] = 9876
print(student_data['Mohan'])

# Deleting the data
# del student_data['Mohan']['phone_no']
# pop also do the same just it return the deleted data.
student_data['Mohan'].pop('phone_no')
print(student_data)

# list in dictionary : 
travel_data = {
    'Gujrat' : ['Dwarkadish', 'Somnath', 'Statue of Unity'],
    'Rajasthan' : ['Jaipur', 'Udaipur']
}

print(travel_data)
print(travel_data['Rajasthan'])

# dictionary within list : 
student_data = [
    {'Name' : 'Ram', 'Roll_no' : 10, 'age' : 20, 'Course' : 'Python'},
    {'Name' : 'Mohan', 'Roll_no' : 20, 'age' : 22, 'Course' : 'Java', 'phone_no' : [23123, 213123]}
]

print(student_data[0])
print(student_data[1]['phone_no'])