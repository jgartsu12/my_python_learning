# Guide to Python's Partition Function
heading = "Python: An Introduction, and Python: Advanced"

first, second, third = heading.partition(': ')
            # prints same as previous commit
print(first) # prints Python
print(second) # prints :
print(third)  # prints An Introduction, and Python: Advanced
# NOTES:
# how parition works 
    # if returnong chapter response from API returns every first value and evertyhing at the end