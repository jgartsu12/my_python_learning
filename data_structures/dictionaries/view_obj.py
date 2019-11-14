# Guide to Python Dictionary View Objects
# view obj --> py3 and > only has --> allows us to peek in and view values and keys of all the diff items within a dictionary
        # view obj reviews the changes in the dictionary
        # dynamic view --> if something changes the view will change for us and keeps it open while someone else at same time is running a query
        # cant treat view objs like a list since it is a view obj
        # what is a view? --> everytime run a query it will run on a thread ... that thread action --> long query takes long time and other user tries to run same query if one tries to make changes to dictionary --> 
        # why these features were built into py
players = {
  "ss" : "Correa", #spaces between : arent need is devper preference
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

print(players.keys()) # --> returns dictionary view objs --> dict_keys(['ss', '2b', '3b', 'DH', 'OF']) 

print(players.values())  # --> returns dictionary view objs --> dict_values(['Correa', 'Altuve', 'Gattis','Bregman']) --> not a list
# cant do: print(players.values()[0]) # --> TypeError: 'dict_values" doenst support indexing --> why not a list --> 

print(players.items()) # returns a tuple of the key:vallue --> dict_items(['ss':'correa', "2b" : "Altuve", "3b" : "Bregman", "DH" : "Gattis", "OF" : "Springer" ])

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}