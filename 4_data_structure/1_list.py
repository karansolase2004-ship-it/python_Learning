# list are mutable : after creating it we can  do the changes

roll_no = [4, 1, 5, 2, 3]
names = ["jenny", "Ram", "Shyam"]
mix_list  = [1, "jenny", True, 10.10]

for each in roll_no : 
    print(each)

print(f"1) {mix_list[0]}")
print(f"2) {mix_list[1]}")

print(f"3) {mix_list}")
print(f"4) {roll_no}")

print(f"5) {len(mix_list)}")

print(f"6) {roll_no[0:]}")
print(f"7) {roll_no[1:4]}") # it work like [1, 4)
print(f"8) {roll_no[1:5]}")
print(f"9) {roll_no[1:5:2]}") #Jumping 2 times from index 1 and printing so on so forth

print(f"10) {roll_no[1:5:3]}")

roll_no.sort() # perform sorting on actual list
print(f"11) {roll_no}")

roll_no.reverse()
print(f"12) {roll_no}")

print(f"13) {min(roll_no)}")
print(f"14) {max(roll_no)}")

# it will sort based on ascii characters where upppercase letters come before lowercase letters 
names.sort()
print(f"15) {names}")

# sort based on lowercase characters :
names.sort(key = str.lower)
print(f"16) {names}")

# Sort cannot be applied on mixlist 

roll_no.append(0) # insert from last 
print(f"17) {roll_no}")

roll_no.insert(0, 6) # (index, value)
print(f"18) {roll_no}")

# to append list to a exisiting list 
roll_no.extend([7, 8, 9, 10, 11, 12])
print(f"19) {roll_no}")

# Modifying the data
roll_no[6] = 1
print(f"20) {roll_no}")

# Modifying data using range : 
roll_no[10:] = [10, 10, 10, 10]
print(f"21) {roll_no}")

# if number passed to remove is duplicate then it will remove first occurence 
roll_no.remove(10)
print(f"22) {roll_no}") 
roll_no.remove(1)
print(f"23) {roll_no}")

# pop remove last element and also print it
roll_no.pop()
print(f"24) {roll_no}")

print(roll_no.pop())

# remove element using the index
print(roll_no.pop(1))
print(f"25) {roll_no}")

# count occureence 
print(roll_no.count(4))

#clear list
print(roll_no.clear())
print(f"26) {roll_no}")