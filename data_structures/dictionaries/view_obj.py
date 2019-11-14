# Guide to Python Dictionary View Objects
# view obj -->  how to treat like a list
players = {
  "ss" : "Correa", 
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

# how to treat view obj like a list
print(list(players.values()))   # convert into list so now can treat like any list
print(list(players.values())[1]) # retrieve index 1 --> Altuve like a normal list

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}