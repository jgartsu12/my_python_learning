# How to Sort Lists [] in Python

totals = [231, 1, 23, 342]

print(totals) # list gets printed in same exact order

totals.sort()
print(totals) # prints them in numeric ascending order --> [1, 23, 231, 342] --- lowest to highest number


tags = ['py', 'dvp', 'tutorials', 'code']

print(tags) # prints in exact order of their index what if u want to sort by their alphabetical value
# lists are muttable
# use sort() to sort backwards; default with dates sorts oldest firsts and then newests
tags.sort(reverse=True)

print(tags) # printed ['tutorials', 'py', 'dvp', 'code'] -- list sort(reverse=True) in reverse-alphabetical order