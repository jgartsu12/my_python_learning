# Three Ways to Remove Elements from a Python List
users = ['J', 'K', 'L', 'M']

print(users)

#secdond method : pop() fn
    # pop - removes very last element but takes the  last item and returns it so u can use the element
popped_user = users.pop() # stores last element in this variaable

print(popped_user)  # returns L
print(users) # prints ['J', 'K', 'L'] 

# use case with pop()
    # process a long list to process payment notice  as u go throug hea list u can go through ea one loop over and pop last one off to send off notification so u dont send that user a duplicate msg
    # used in alg