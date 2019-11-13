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

#query specific elemnts inside of list - how to get access to the list
print(users[2])
    # prints Tiffany w/o [ ]; thus is no longer a list object; returns string object Tiffany

print([users[2]]) # prints ['Tiffany']