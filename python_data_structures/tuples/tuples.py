# Intro To Python Tuples

# Data Types:
    # List: []
    # Dictionary: {}
    # Tuple: ()

# Differences btween tuples and lists

# why u would use tuple or list
    # is this a data structure I want to change or not ???? 
    # Tuple: immutable - cannt change
    # List: mutable - can change
    # machine learning more ctrl over ur data structures in python

# sample tuple   3 elements inside of the tuple = title, subheading, content
post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

post.sort() # => cant sort() a tuple ==> AttributeError 

# Tuple unpacking - py will treat each one of these items as a QUERY ENGINE
title, sub_heading, content = post # process will work the same way with a list but u dont do this: 

# Equivalent to Tuple unpacking - query engine like => works exactly same way as above
# title = post[0]
# sub_heading = post[1]
# content = post[2]

# gives us access to each one of these elements
print(title) 
print(sub_heading)
print(content)

# above tuple as a list to see differences
post = ['Python Basics', 'Intro guide to python', 'Some cool python content']

post.sort() # this prints 'intro guide to python' as the title ... 'python basics' as the subheading and content is the same 
            # top reason u wouldnt want to use a list when using this type of unpacking
                    # if order changes = > unexpected beh in the order

more notes:
    # with strings are immutable can onlt reassign a str