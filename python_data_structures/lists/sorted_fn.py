# Guide to the sorted Function in Python
# using sorted() method
    #sorted() allows u to store that new value in a new variable that stores that list and keeps original list stored
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

sorted_list = sorted(sale_prices, reverse=True) # sorted(argument_list, reverse order)

print(sorted_list) # prints [400, 220, 100, 100, 83, 40, 10, 3, 1] # can set sorted() with reverse in descending integer order
