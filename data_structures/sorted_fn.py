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

sorted_list = sorted(sale_prices) # sorted(argument_list)
            # demonstrates that orignal list stays saved with sorted()
print(sorted_list) # prints [1, 3, 10, 40, 83, 100, 100, 220, 400] not none
print(sale_prices) # prints original list in same order : [100, 83, 220,40, 100, 400, 10, 1, 3]
