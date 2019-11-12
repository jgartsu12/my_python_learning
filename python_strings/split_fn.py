# split fn - used qd devmnt - single delimator - seperates str into 2 parts
# split vs partition
tags = 'python,coding,programming,development'

# tags = tags.split() poor practice - split returns a list of elements => bugs 
list_of_tags = tags.split(',')
print(list_of_tags) # prints ['python', 'coding', 'programming', 'development'] this is the list