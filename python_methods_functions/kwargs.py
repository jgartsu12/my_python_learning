# Overview of Keyword Arguments in Python Functions
# kwargs => keyword arguments => returns dictionary cuz a dictionary needs key and values
def greeting(**kwargs):
    print(kwargs)


greeting() # => {} a dicitionary

# ~~~~ 

def greeting(**kwargs):
    print(kwargs)


greeting(first_name ='JJ', last_name = "ll") # {'first_name': 'JJ', 'last_name': 'll'} 
            # {'key' : value ' , 'key'    :  'value'}
# ~~~~~~~~~

# user vs guest in a greeting 
def greeting(**kwargs):
    if kwargs:
        print(f"Hi {kwargs['first_name']} {kwargs['last_name']}, have a great day!")
    else:
        print(f"Hi Guest, have a great day!")


greeting(first_name ='JJ', last_name = "ll") # => Hi JJ ll, have a great day! || (if)
greeting()  # => Hi Guest, have a great day! || (else)