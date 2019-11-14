# Guide to Using the get Function in Python Dictionaries to Configure Fallback Lookup Values
teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts'],
} 

teams['astros'] # performs query

featured_team = teams['astros'] # storing query in a variable

print(teams)