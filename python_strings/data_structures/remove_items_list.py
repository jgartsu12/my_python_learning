# Three Ways to Remove Elements from a Python List
users = ['J', 'K', 'L', 'M']

print(users)

#first method : remove() fn
    # remove('str wanted to remove')
users.remove('J')

print(users) # prints ['K', 'L', 'M']