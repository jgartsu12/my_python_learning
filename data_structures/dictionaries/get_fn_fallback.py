# Guide to Using the get Function in Python Dictionaries to Configure Fallback Lookup Values
teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts'],
} 

featured_team = teams['mets'] # try looking for a key not in the dictionary returns KeyError: "mets"
                                                                                            # no key name "mets" in the dictioanary
print(teams)