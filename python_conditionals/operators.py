# Full List of Python Conditional Operators
       # List of comparison operators: -- what we put inside of condition to check 
            # == Equality --> equal to
            # != Inequality --> not equal to
            # <> Inequality (deprecated) --> no longer being worked on py doesnt use it 
            # >  Greater than
            # >= Greater than or equal to
            # <= Less than
            # <= Less than or equal to

# test value ranges
# dynamic beh
# full true/false outcomes

# ~~~~~~~~~~~
# username = 'jonsnow'

# if username == 'jonsnow': # if true print
#     print('Welcome')
# else: # if false print
#     print('U shall not pass!') # => Welcome since conditition is true
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# username = 'jonsnow'

# if username != 'jonsnow': # if true print (if username is not jonsnow)
#     print('Welcome')
# else: # if false print 
#     print('U shall not pass!') # this prints => U shall not pass! since username is  == jonsnow
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# condition checks for simply true or false value
# username = 'harrypotter'

# if username != 'jonsnow': # if true print (if username is not jonsnow)
#     print('Welcome')
# else: # if false print 
#     print('U shall not pass!') # => Welcome since username doesnt == jonsnow

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# age = 55

# if age != 90:
#     print('Young')  # returned ==> Young
# else:
#     print('old')

# #~~~~~~~~~~~~~~~~~~
# username = 'jonsnow'

# if username > 'jonsnow':
#     print('Welcome')
# else:
#     print('U shall not pass!') # returned ==> u shall not pass! --> makes no since
                                    # string should not be compared with one being > than other
                                    # strings use the inequality or eqaulity 
#~~~~~~~~~~~~~~~~~~~~~~

# age = 55

# if age > 10:
#     print('not super young')  # returned ==> not super young
# else:
#     print('reallt young')

#~~~~~~~~~~~~~~~~~~~~~~~~
#   lists with conditionals and operatrs
# ---------------------------------------
# user_list = ['Kristine', 'Tiffany']
# second_list = ['jk', 'lol']

# if user_list == second_list:
#     print('They match') # nothing printed cuz lists dont match

#~~~~~~~~~~
user_list = ['jk', 'lol']
second_list = ['jk', 'lol']

if user_list == second_list:
    print('They match')    # => They match
    # why compare two identical lists?? -> build out alg looking for duplicates .. checking to see if historical data matches with test data current