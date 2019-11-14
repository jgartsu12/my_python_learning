# Guide to Using the get Function in Python Dictionaries to Configure Fallback Lookup Values
teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts'],
} 
# .get() fn takes in to arguments -- ('key searching for', 'backup value if not there')
featured_team = teams.get('mets', 'No featured team')

print(teams) # returns "No featured team" --> best py practice to provide u with instant feedbacjk to tell u it is not in the dicitonary 