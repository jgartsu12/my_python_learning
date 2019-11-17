# How to Build Compound Conditionals in Python
# multiple conditions in a py program

# AND Operator --> more restrictions
# OR operator -- more flexibility
# ~ AND NOT operator 

# username = 'sansa'
# email = 'jon@snow.com'
# password = 'thenorth'

# if username == 'jonsnow' and password == 'thenorth':          # both condition on right and left of 'and' must be true
#     print('Access Granted') # => returned
# else:
#     print('Accessed Denied!')

# if username == 'jonsnow' and password == 'thenorth':         
#     print('Access Granted') 
# else:
#     print('Accessed Denied!') # => returned

# without and operator --- nested if else conditional
# if username == 'jonsnow': 
#     if password == 'thenorth':         
#         print('Access Granted') 
# else:
#     print('Accessed Denied!') # ==> 

# ~~~~~~ # OR OPERATOR ~~~~ what if we dont want both items required want one to be true
# if username == 'jonsnow' or password == 'thenorth':    # works if username is false      
#     print('Access Granted') # => returned even when username is not 'jonsnow'
# else:
#     print('Accessed Denied!') 
    # or op is more flexible operator
    # not a logical sys 

# third condition --> type in ur username or email like github ... more flexible could have username or email to login
# uses both or and 'and' operator
    # this will split up the operators using order of operation - parens first -- treated as single expression --> if one is true btween or - u  can access site

# username = ''
# email = 'jon@snow.com'
# password = 'thenorth'

# if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':         
#     print('Access Granted') # => returned
# else:
#    print('Accessed Denied!')

# username = 'jonsnow'
# email = 'jon@snow.net'
# password = 'thenorth'

# if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':         
#     print('Access Granted') # => returned
# else:
#    print('Accessed Denied!')

# username = 'jonsnow'
# email = 'jon@snow.cpm'
# password = 'north'

# if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':         
#     print('Access Granted') 
# else:
#    print('Accessed Denied!')# => returned

## ~ AND NOT operator - see if one side is True and otherside False
# logged_in = True
# standard_user = True # permission lvl user can have
# # if True and not False: .... (NOT TRUE = False)
# # left side of and not = True ... right side o and not = False
# if logged_in and not standard_user:
#     print('U can access admin dashboard')
# else:
#     print('U can only access standard dashboard')# => returned

logged_in = True
standard_user = False # permission lvl user can have
# if True and not False: .... (NOT TRUE = False)
# left side of and not = True ... right side o and not = False
if logged_in and not standard_user: # (TRUE)
    print('U can access admin dashboard') #=> returned
else: # (FALSE) 
    print('U can only access standard dashboard')