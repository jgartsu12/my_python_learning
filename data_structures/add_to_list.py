# How to Add to a List in Python with Both In Place and Copy Processes
tags = ['python', 'development', 'tutorials', 'code']
# algorithms when iterating over a list makes u add elements to the list while looping through it
# key differences between In Place vs Copy

# how can we store it in new variable
# THIS IS NOT IN PLACE and does not alter the first variable with list stored in it
new_tags = tags + ['Programming'] ## adds programming tot he end of the previous list --> must be wrapped in ['str']

# cant do:
new_tags = tags + 'Programming' # - cant add a string to a list since they are diff data types --> str vs ['list']

print(new_tags) # --> returns ['python', 'development', 'tutorials', 'code', 'Programming']

print(tags) # --> returns  ['python', 'development', 'tutorials', 'code'] still 