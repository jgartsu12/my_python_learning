# How to Combine All Argument Types in a Single Python Function
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def greeting(time_of_day, *args, **kwargs): # args will be username
    print(f"Hi {' '.join(args)}, I hope you are having a great {time_of_day}")

    if kwargs:
        print('Your tasks for day are:')
        for key, val in kwargs.items():   # for/in loop over a dictionary
            print(f"{key} => {val}")  # => is the task

# large amount args pass args on diff line
greeting('Morning',     # time_of_day (positional args)
'Krisitne', 'Hudgens',  # *args --> tuple 
first = 'Empty dishwasher', # first, second, third = **kwargs
second = 'Take pupper outside',
third = 'Math HW')  

# prints: 
''' 
Hi Krisitne Hudgens, I hope you are having a great Morning
Your tasks for day are:
first => Empty dishwasher
second => Take pupper outside
third => Math HW
'''