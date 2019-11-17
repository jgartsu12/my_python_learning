# Basic Syntax for Creating Python Functions
# def => define function
# use snakecase like creating variables

#  basecase
# def full_name():
    # print('Hi')
# space
# standard conv: two lines of space btwen function defintion and next code
# full_name() # returned => Hi in terminal

# fn with fn arguments => allows u to pass in values to pass in diff objts (can pass in lists ...)
# def full_name(first, last):
#     print(f'{first} {last}')
# # space
# # space
# full_name() 
# # TypeError: full_name() missing 2 required positional arguments: 'first' and 'last'
# need to pass in arguments  so no error

def full_name(first, last):
     print(f'{first} {last}')
# # space
# # space
full_name('Kristine', 'Hudgens') # => Kristine Hudgens
full_name('J', 'Low') # => J Low
# can call functions anywher else in ur program

def auth(email, password):
    if email == 'kristine@h.com' and password =='secret':
        print('authorized')
    else:
        print('DENIED!')
# space
# space
auth('jmoney@h.com', 'secret') # => DENIED
auth('kristine@h.com', 'secret') # => authorized

# function w/ no arguments
def hundred():
    for num in range(1,101):
        print(num)


hundred()  # => all numbers btwn 1 - 100
#~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~ ~~
def counter(max_value):
    for num in range(1,max_value):
        print(num)


counter(501) # => returns all numbers btween 1 - 500