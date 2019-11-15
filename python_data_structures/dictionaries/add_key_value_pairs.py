# How to Add New Key/Value Pairs to Python Dictionaries -- continuing nested colelctions
teams = {  # teams dictionary  with key being the team, value [players list]
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels" : ["Trout","pujols"],
  "yankees" : ["judge", "stanton"],
}

teams['red sox'] = ['Price', 'Betts'] # can have multiple words in ' key name ' --> keys can be treated like "strs - u can write anything explicit here pref"

print(teams) # added red sox to teams dictionary 