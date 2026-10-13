# In Python, the pass statement is a null operation—meaning it does absolutely nothing when it executes

# it is used as placeholder for future code 

# use case of pass 

def fetch_api_data():
    pass

class MyCustomError(Exception):
    pass

for item in database:
    if item.is_valid():
        # Do something
        print("Valid item found")
    else:
        pass

for i in [1, 2, 3]:
    if i == 2:
        pass
    print(i)