# Introduction to the Python Set Data Structure
# set = hybrid list and dicitonary syntax- like
# no key value pairs
# set = collection of unique elements to see what exists

tags = {
    'python',
    'coding',
    'tutorials'
}

print(tags)
# returns => set: {'python', 'coding', 'tutorials'}

# all elements inside of a set are unique
    # set = no duplicates
tags = {
    'python',
    'coding',
    'tutorials',
    'coding'
}

print(tags) # => returns {'python', 'coding', 'tutorials'} w/o coding twice

# how to not query our set
#TypeError 
print(tags[0]) # => TypeError: 'set' obj doenst support indexing

# query our set
query_one = 'python' in tags
query_two = 'ruby' in tags 

print(query_one) # returns => True || python exists in the set
print(query_two) # => False || doesnt exist in the set