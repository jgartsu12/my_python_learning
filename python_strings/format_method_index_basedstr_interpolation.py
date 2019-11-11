name = 'Kristine'
age = 12
product = 'Python eLearning course'
from_account = 'Jordan'

# greeting = "Product Purchase: {2} - Hi {0}, you are listed as {1} years old. - {3}".format(name, age, product, 'Jordan')

# str literal version: 
greeting = f"Product Purchase: {product} - Hi {name}, you are listed as {age} years old. - {from_account}"
                        # dont have to worry about using index values using str literals!!

print(greeting) # prints same as w/o str literal