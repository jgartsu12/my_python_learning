# How to Use Python's format method to Implement Index Based String Interpolation
name = 'Seb'
age = 12
product = 'Python eLearning Course'

greeting = "Product Purchase: {2} - Hi {0}, you are listed as {1} years old and you have purchased: {2} - {3}".format(name, age, product, 'John')
# order doesnt matter just has to be mapped to right index value in .format(argument0...)
print(greeting)
# prints : Product Purchase: Python eLearning Course - Hi Seb, you are listed as 12 years old and you have purchased: Python eLearning Course - John
