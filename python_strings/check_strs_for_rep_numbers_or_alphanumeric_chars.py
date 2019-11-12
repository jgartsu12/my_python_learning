# How to Check if Strings Represent Numbers or Alphanumeric Characters in Python
api_data = '5' # string with 5 inside
greeting = 'Hi '

# isnumeric() fn
print(api_data.isnumeric()) # prints True
print(greeting.isnumeric()) # prints False
#Notes
# 5 is a string with a number thus it is numeric so its True
# use isnumeric() in db query to get integer instead of false positives