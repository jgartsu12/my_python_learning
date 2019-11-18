# How to Utilize Named Function Arguments in Python

# posititional args: mapping value and how value is used in exact order they are put in
                        # ex. J => first ... Low => last
            # ORDER MATTERS IN POSITIONAL ARGS (POSITION)
            # NOT GREAT FOR BIG PROGRAMS WITH MANY ARGUMENTS
            #POSITION DETERMINES THE MAPPING 
def full_name(first, last):
  print(f'{first} {last}')


full_name('J', 'Low')

# NAMED ARGS ALLOW U TO BE MORE EXPLICIT WITH UR ARG

def full_name(first, last):
  print(f'{first} {last}')
# more explcit when passing values in
# position no longer matters
full_name(last = 'Low', first = 'J' ) # first looks for fn arg named first and then fn arg named last
# named arg can be used in optional manner in py unlike ruby
# more than 2 args use named arguments to prevent bugs 