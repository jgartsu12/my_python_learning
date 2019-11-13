# Guide to Nested Lists and Best Practices for Storing Multiple Data Types in a Python List
users = ['K', 'T', 'J', 'L']

ids = [ 1, 2, 3, 4]

mixed_list = [42, 32.2, 'Alutve', users]

#can call list fns on the nest list as well: 
user_list =mixed_list.pop()
print(user_list) # prints [42, 32.2, 'Alutve']