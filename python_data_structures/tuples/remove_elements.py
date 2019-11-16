# Three Ways to Remove Elements from a Python Tuple
#  tuples are immutable so original is not having anything removed but the new ones will be new tuples with elements removed
# real world situation u didnt create the tuple but working with outsdie library with collection and cant ctrl tuple is what u have to work w/
# if changing tuple constantly .. then ask self should this be a list [] ??

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# FIRST WAY : reassignment: Removing Elements From End
    # slice  - returns element u want to keep
post = post[:-1] # this will take everything but the last element

print(post) #=> prints everything but 'published' and 'some cool content'

# second way: remove elements from beginning
post = post[1:] 

print(post) # => ('Intro guide to Python', 'Some cool python content', 'published')

# 3rd way: removing specific element (messy/not suggested) ~ cast to different data type
    # reassigment and convert to list
    # casting into tuple into a list
post = list(post) # bad idea => say u dont change it back to a tuple and call fns that only works w/ tuple u get bugs due to diff data types
post.remove('published')
post = tuple(post)  # converts/ casts back to tuple with published removed

print(post) # prints ['Python Basics', 'Intro guide to Python', 'Some cool python content', 'published']
                # now we can treat tuple like a lists since now it is a list
