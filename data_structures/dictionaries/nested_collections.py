# Guide to Nested Collections in Python Dictionaries
# key value pair can have collection of values :
        # key-value pair can only be 1-1 pair but the value can have a collection like an []
        # helpful-->  break elements to lowest form possible look and dissect into to chunk to know how to work with ea element such as variable, assignment, lists ... dictionaries {key:value}
teams = {  # teams dictionary  with key being the team, value [players list]
  "astros": ["Altuve", "Correa", "Bregman"]
}

print(teams['astros'][0]) #use slice to get return --> Altuve