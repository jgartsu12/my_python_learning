# Working with Lists Nested in Tuples
# add new element that is a list inside of the tuple 
# tuples are immutable ... lists are mutable !!
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content') # tuple

tags = ['python', 'coding', 'tutorial'] # list w/ 'strs'

post += (tags,)  # performed reassignment to pass in new tuple with the variable tags that stores a list [ ]

print(post) # returns => ('Python Basics', 'Intro guide to Python', 'Some cool python content', ['python', 'coding', 'tutorial'])
        # traverse tuple with a nested list
            # web  or mobiles api (use)
print(post[-1]) # returns => ['python', 'coding', 'tutorial']
print(post[-1][1]) # returns =>  coding 