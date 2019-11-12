# split fn - used qd devmnt - single delimator - seperates str into 2 parts
# split vs partition
heading = "Python: An Introduction"

heading_list = heading.split(': ')
print(heading_list) # prints --> ['Python', 'An Introduction']
# partition returns a tuple; split returns a list 
    # key diff --> very easy to perform variable deconstruction (done with partition ... tuple)
        ## API structure used easily with tuples to var deconstruct it
    # split more flexible works with wider array of strings
        # split allows u to break up string into independent elements in a list
        # split used most of the time 