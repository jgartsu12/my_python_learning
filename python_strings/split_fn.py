# split fn - used qd devmnt - single delimator - seperates str into 2 parts
# split vs partition
tags = 'python,coding,programming,development'

# tags = tags.split() poor practice - split returns a list of elements => bugs 
list_of_tags = tags.split()
print(list_of_tags) # prints ['python,coding,programming,development']
# now u can work with this data as a collection
# split without default converts u string into a single element in a list 