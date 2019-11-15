# Guide to Python Dictionary View Objects
# view obj -->  thread safety
players = {
  "ss" : "Correa", 
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

# thread safety - thread safe (senior-lvl-dvp) make quick copy of list and then perform our actions
# use of copy() fn --> perform any actions u want without data change
player_names = list(players.copy().values())

print(player_names) # prints players {} values aka name of the players
                        # only we can access these players stored
teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}