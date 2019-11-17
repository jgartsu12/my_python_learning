# How to Implement Python Loops for Lists, Tuples, and Dictionaries
# iterate through collections of data using looping
        # LISTS
players = ['Altuve', 'Bregman', 'Correa', 'Gattis'] # lists of strs

# FOR IN LOOP # 2-4 spaces - indentation needed in py (block)
# common convention players mapped to the variable with the collection;;; player can be named anything it is a iterator/block variable
# iterates with number of things in the [ ]
# common convention the iterator variable is a single form of the name of collection variable
for player in players: 
    print(player) #  => Alutve Bregman Correa Gattis

# for x in players 
#     print(x) # prints same as above

# for square in squares: # for singular_form in plural_form: --> common conv

# TUPLES
# above works same with a TUPLE:
players = ('Altuve', 'Bregman', 'Correa', 'Gattis') # tuple of strs 

for player in players: # => returns same as lists -- works same way as lists do..
    print(player)

# Dictionaries FOR/In LOOPS -- need to grab key and the value
players = {
    '2b' : 'Altuve',
    '3b' : 'Bregman',
    'ss' : 'Correa',
    'dh' : 'Gattis'
}
        # two variables- firstt iteration is the position aka the key; second iteration is player which is the value
for position, player in players.items(): # items creates dicitonary view to grab access to all the items 
    print('Position', position)
    print('Player Name', player) 
                """ returns = > 
                                Position 2b
                                Player Name Altuve
                                Position 3b
                                Player Name Bregman
                                Position ss
                                Player Name Correa
                                Position dh
                                Player Name Gattis
                """