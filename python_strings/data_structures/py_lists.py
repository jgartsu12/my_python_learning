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

# .append("add string to list")
users.append('Ian')
print(users) # prints list with Ian added to the end of the list