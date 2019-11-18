# How to Nest Functions in Parent Functions in Python
# py diff from other languages since it allow u to put a fn inside another fn

def greeting(first, last):
    def full_name(): # since nested in greeting doesnt need both arugments
        return f'{first} {last}'

    
    print(f'Hi {full_name()}!')


greeting('Kristine', 'Hudgens') # now pass in first and lastname wanted
            # => Hi Kristine Hudgens!

# When to use nested fn vs keep seperate ?
    # fn that doesnt need to exist outside of parent fn
        # ex. never needed to call full_name fn except in the greeting fn then no need to put in another part of the application ... 
        # if needed in another part of the program dont nest