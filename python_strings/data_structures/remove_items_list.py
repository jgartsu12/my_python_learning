# Three Ways to Remove Elements from a Python List
users = ['J', 'K', 'L', 'M']

print(users)

# 3rd method : del 

del users[0] # argument is index value  u want to remove
 # use case - know list and its index value and u want to remove that value
print(users)
    # deletes 0 index which is 'J' so it prints ['K', 'L', 'M']