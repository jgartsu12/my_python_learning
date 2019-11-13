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

#place new element into the list #insert (index_for_placement_value, "inserrted str")
users.insert(0, 'Anthony') 
print(users)  #makes list 4 elements with Anthony before John