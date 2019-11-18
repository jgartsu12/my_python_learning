# Guide to Default Arguments in Python Functions

def greeting(name):
    print(f'Hi {name}!')


greeting() # prints an error no positional argment
greeting('Kristine') => Krisin

# ~~~~~~~
# default arg set up in fns
def greeting(argument = 'Default arg'):
    print(f'{name}!')


greeting() # prints hi default arg!
greeting("j low") # overides default arg

#~~~~~~~~~~
# python interview question**
def some_function(collection = []): # expects list as its argument
    collection.append(1)  # goes to our collection and appennds 1
    return collection # warning dangerous default value [] as argument
                            # immutability vs mutability
                            # dont want to make a mutable data type like list a default arg**
print(some_function()) # = [1]

# call at another part in program in another file diff part in the app
print(some_function()) # => [1, 1]
    # our collection iis staying in memory so even if calling fn at another part of program it will go reference the collection in memory
    # connection btwn ln 26 and 29 in memory

### dont do: 
def some_function(collection = []):
  collection.append(1)
  print(id(collection)) # id => place in mempry on ur computer
  return collection


print(some_function())
print(some_function()) # => both ref the same id so list was just added on to same one in memory