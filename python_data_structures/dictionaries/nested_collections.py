# Guide to Nested Collections in Python Dictionaries
# key value pair can have collection of values :

        # key-value pair can only be 1-1 pair but the value can have a collection like an []
        # helpful-->  break elements to lowest form possible look and dissect into to chunk to know how to work with ea element such as variable, assignment, lists ... dictionaries {key:value}
                # complex programming = foundational stuff broken down
teams = {  # teams dictionary  with key being the team, value [players list]
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels" : ["Trout","pujols"],
  "yankees" : ["judge", "stanton"],
}

astros = teams['astros'] # can store that dictionary in a variable as well

print(astros)
print(teams['yankees'])
print(teams['astros'])
print(teams['angels'])

