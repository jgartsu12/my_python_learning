# Overview of the Multiple Methods for Deleting Items in a Python Dictionary

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

# first way with del key word
    # del name_of_dic['key to delete'] --> must know key is in the dict
del teams['astros'] # deletes 'astros' from dictionary

#key error
del teams['mets'] #KeyError: 'mets" since mets isnt key in the dicitonary

#key error - use default fall back value with .get
print(teams.get('mets', 'no team found by that name')) # provides this fixed output since 'mets' isnt a key

print(teams)

# pop()
teams.pop('astros', 'No team found by name') # astros was deleted --> astro 
teams.pop('rays', 'no key named such') # no output but original dictionary
                                            # where does this go? pop() returns a value of lookup or default fallback value must store in a var

removed_team = teams.pop('rays', 'no key named such') 
removed_team_two = teams.pop('yankees', 'no key named such')

print(teams)
print(removed_team) # returns the dicitonary and the default fallback 'no key named such'
print(removed_team_two) # returns dictionary w/o yankees