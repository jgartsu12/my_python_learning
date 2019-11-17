# Guide to Continue and Break in Python Loops

usernames = [ # list of GOT usernames represented as strings in the usernames variable
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

# 2 CONTROL FLOW OPERATORS:
        # 1. Continue
for username in usernames: # find cersei and have different output if someone else.. blacklisted users/banned users and want to know who they are ==> pracitcal exp
    if username == 'cersei':                     # conditional nested code inside it
        print(f'Sorry, {username}, you are not allowed')
        continue
    else:
        print(f'{username}, is allowed')
        ''' returns =>
                    jon, is allowed
                    tyrion, is allowed
                    theon, is allowed
                    Sorry, cersei, you are not allowed
                    sansa, is allowed
            notes on continue: continues after cersei eventhough she is not allowed
                    # continue --> in loop it finds the condition if true it changes behavior; continue tells the program to keep going through loop and not stop once it finds what is looking for
                    # oppoiste of break behavior 
                    # continue --> program keeps going
        '''
        # 2. Break
for username in usernames: 
    if username == 'cersei':                    
        print(f'{username} was found at index {usernames.index(username)}') 
        break # anything after a break will not happen if nested after this code block
    else:
        print(username)
    ''' returns =>
                    jon
                    tyrion
                    theon
                    cersei was found at index 3
    
    Notes -> break = search and destroy if u find username looking for it stops at that condition
                # it stopped at cersei since condition was found thus not printing sansa
                # stops once condition found === BREAK
                # breaks out of the loop
    '''