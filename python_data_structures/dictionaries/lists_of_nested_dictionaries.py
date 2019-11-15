# Guide to Working with Lists of Nested Dictionaries
# how one collection can store another collection (web mobile apps; machine learning ...)
# teams db: list w/ various dictionariies
# use  case studies to test this out and get used to this to work with API data and db queries!! TO DO (**(*))
teams = [ # list with nested dicitionary with more nested collecctions
  {   # dictionary 1
    'astros': { # key : value         # index 0
      '2B': 'Altuve', # elements
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {   # dicitionary 2
    'angels': {           # index 1
      'OF': 'Trout',
      'DH': 'Pujols',
    }
  }
]

print(teams[0]) # prints astros dictionary
'''
{   
    'astros': { # key : value         # index 0
      '2B': 'Altuve', # elements
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  } 
'''

angels = teams[1].get('angels', 'team not found')

print(angels)
# returns :
''' 
{   
    'angels': {           # index 1
      'OF': 'Trout',
      'DH': 'Pujols',
    }
  }
'''
                                                # idx 0    # idx 1
print(angels.values()) # returns: dict_values(['Trout', 'Pujols'])

print(list(angels.values())) # ['Trout', 'Pujols']

print(list(angels.values())) # returns Pujols # took 4 levels similar to finding api data query
# take nested data strucuture a piece at a time

