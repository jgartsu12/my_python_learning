def guessing_game(): # user guesses until right answer is guessed
    while True:
        print('What is your guess?')
        guess = input()    # sets up prompt into terminal and store what evers written into it

        if guess == '42':
            print('You guess correctly')
            return False # continues to be true until told it is false ==> SENTINEL value to stop while loop
        else:
            print(f'No, {guess} is not correct, please try again\n') # \n gives new line so user can guess on new line

guessing_game() 