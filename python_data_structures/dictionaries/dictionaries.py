# Overview of Python Dictionaries
# dictionary -> key value data store - can create key with a corresponding value -> use curly braces { }
        # to access key : value data u pass in the key instead of the index for dictionaries
players = {
    "ss": "Correa", # --> key : value pair
    "2b": "Altuve",
    "3b" : "Bregman",
    "DH" : "Gattis",
    "OF" : "Springer",
}

second_base = players['2b']

third_base = players['asdf'] # error cuz that key isnt in the dictionary

designated_hitter = players['DH'] # returns 'Gattis' 
print(players) #--> returns {'ss': 'Correa', "2b": "Altuve", "3b" : "Bregman", "DH" : "Gattis", "OF" : "Springer"}
print(second_base) # ==> returns  'Altuve'
print(third_base) # --> returns : KeyError 'asdf'  (not a scilent bug)
                        # --> helpful because tells u its not a key other programming lang may not be as helpful of indicating the error (py references key error)
                            # when accessing keys they are case-sensitvie