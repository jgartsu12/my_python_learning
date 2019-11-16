# Guide to Python's Zip Function
# fn is in py core library -- merge lists or multiple lists into tuples
# data sci and machine learning algorthims use these for matrixxes ==> nest collections
# sorted order of ur list is important so they merge properly with zip fn ***
        # why order matters: 2b mapped to altuve ... 3b mapped to bregman .. . etc. .. etc..
                # zip allows us to merge these automatically
positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']
scoreboard = zip(positions, players)

# print(scoreboard) # prints <zip object at id#> ... -> so need to convert to a list
print(list(scoreboard)) 
        # prints ==> [('2b', 'altuve'), ('3b', 'Bregman'), ('ss', 'correa'), ('dh', 'gattis')]
                    # list with set of 4 tuples
                    # direct mapping 
                    # machine learning data processing
                    # API ecom app - merge elements
                    