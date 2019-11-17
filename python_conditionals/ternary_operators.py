# How to Use the Ternary Operator in Python Conditionals
# need to be careful where  u use these ... PEP 20 3rd item simple is better than complex
# if ternary op can read like normal language then its good time to use it 
# reorganzies  a typical conditional works for us

role = 'person111'

# auth = 'can access' if role == 'admin' else 'cannot access'

# print(auth) # => can access
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
