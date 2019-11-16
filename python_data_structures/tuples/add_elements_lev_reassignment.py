# How to Add Elements to a Tuple by Leveraging Re-Assignment
# leverage reassignment to create a new tuple  
# tuples are immutable !!
            # title                 #subheading         # content
post = ('Python Basics', 'Intro guide to python', 'Some cool python content') # hard coded tuple 
                        # this will come from databases and api with tons of data u cant see al or know all
print(id(post)) 
        # different id from below because it is another object
# post = post + ('published') # this wouldnt be treated like a tuple but a math expression pemdas such as (2*2) + 5 => order of ops == > TypeError can only concat a tuple with another tuple -- it views it as a str + tuple
# post = post + ('published',) # so to not treat liek order ops need a ',' so python treats it like a tuple
                                # overrides to make a new one

post += ('published',)  # mass assignmnet operator -- eqaul to post = post + ('published',) 

print(id(post))  # id function in python - gives references and unique id for an object -- in memory there is a very specific spot in memory where every obj is stored
                    # prints specific id for this post stored in memory (long identifier with numebrs)
                # this id is not the same as the original tuple since they are different tuples due to reassignment --- IMMUTABLE ---
title, sub_heading, content, status = post # tuple unpacking # added status by making a new tuple called status via reassignment and override it

print(title)
print(sub_heading)
print(content)
print(status)