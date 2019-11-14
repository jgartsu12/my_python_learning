# Guide to the sorted Function in Python
# sort list and not change original list
sale_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3
]

sorted_list = sale_prices.sort() # store new list in a variable

print(sorted_list) # prints None --> sort() fn doesnt return a value