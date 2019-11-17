# How to Use the Ternary Operator in Python Conditionals
# need to be careful where  u use these ... PEP 20 3rd item simple is better than complex
# if ternary op can read like normal language then its good time to use it 
# reorganzies  a typical conditional works for us

role = 'person111'

auth = 'can access' if role == 'admin' else 'cannot access' # ternary op - if too many lines use conditional
# assigning result of ternary operator if condition is true else condition false print this code
# var = 'print this' if var == True else "print if false" then store it
print(auth) # => can access

# ~~~~~~~~~~~~~~~
# role = 'guest'

# auth = 'can access' if role == 'admin' else 'cannot access'

# print(auth) # => cannot access

# ~~~~ comparision of ternary op to conditional
if role == 'admin':
    auth = 'can access'
else:
    auth = 'cannot access'

print(auth) # prints cannot access
