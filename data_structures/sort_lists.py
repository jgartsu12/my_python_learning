# How to Sort Lists [] in Python
tags = ['py', 'dvp', 'tutorials', 'code']

print(tags) # prints in exact order of their index what if u want to sort by their alphabetical value
# lists are muttable
# use sort() to sort backwards; default with dates sorts oldest firsts and then newests
tags.sort(reverse=True)

print(tags) # printed ['tutorials', 'py', 'dvp', 'code'] -- list sort(reverse=True) in reverse-alphabetical order