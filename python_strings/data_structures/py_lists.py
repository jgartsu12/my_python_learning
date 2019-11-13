""" notes: array = [list] in python [ ] 
User DB query - work with lists like ones connected with db to see what gets returned from db query
John
Seb
Ken
['str','str',.... 'str']
"""

users = ['John', 'Seb', 'Ken']
# strings are immutable but lists muttable - u can change lists
print(users) # prints the user with true data structure -- list of str names

# edit the list
    # perform standard assignment - find element with index of four and assign t his value
users[1] = 'Jan'
print(users) # prints ['John', 'Jan', 'Ken']