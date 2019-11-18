# What Does it Mean to Return a Value from a Python Function?
# print vs return statement
# how to pass values around in py
# only use print when using debuggin when want to see output of a fn
# in program print just prints to the logs not to like a front end React app
# input and output of process -> very clear w/ fn's

# return
def full_name(first, last): # first and last are our inputs
    return f'{first} {last}' # returns value that makes this useful 
                            # no longer just prints to console but simply returns a value

j_low = full_name('J', 'Low') # called our fn in variable and then use just like a regular str

def greeting(name):
    print(f'HI {name}!')         # in real life u will have perform other tasks like showing it on a web page (render on webpage)
                        # call from another part in a program

greeting(j_low)  # returns HI J Low!

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# print
def full_name(first, last):
    print(f'{first} {last}') # prints name ==> J Low
 

j_low = full_name('J', 'Low') 

def greeting(name):
    print(f'HI {name}!')         # prints ==> HI None! since when simply printing value out in a fn returns nothing since chrinstine is storing none


greeting(j_low)

