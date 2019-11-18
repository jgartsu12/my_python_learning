# Guide to Function Argument Unpacking in Python
    # fn takes in collection of data and dont know how much qty data is coming in
    # def fn_name(*args) =-> unpacking fn - tuples of items
            # machine learning algorithms use this unpacking
   
def greeting(*args): # fn declaration
    print('Hi ' + ' '.join(args))

greeting('J', 'Low') # => Hi J Low # 2 (args)
greeting('J', 'C', 'LOWWW') #=> Hi J C LOWWW # 3 args

#~~~~~~~~~~~~~
def greeting(*args):
    print(args)

         # (TUPLES) <=> unpacking <=> argument lists
greeting('testing', 'one') # => ('testing', 'one')  # a tuple
greeting('testing', 'two') # => ('testing', 'two')  # tuple

#~~~~~~~~~~  # *args is common convention and best practice but not required keyword
# dont do:
# def greeting(*names):
    # print('Hi ' + ' '.join(names)) # join allows u to take in a collection

#~~~~ not limited to only passing in collection of data
# greeting and time of day
# positional arg (must be first arg) and args
def greeting(time_of_day, *args):
    print(f"Hi {' '.join(args)}, I hope that you having a good {time_of_day}")

greeting('Morning', 'J', 'C', 'Low') # => Hi J C Low, I hope that you having a good Morning
greeting('Evening', 'MJ', 'Brown') # => Hi MJ Brown, I hope that you having a good Evening
