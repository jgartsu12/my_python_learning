# How to Find the Median of a Python List with an Odd Number of Numbers
'''
Tools:
- math library
- sorted function
- list slicing
- computations
'''
import math

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

#sorted method to sort lists
sorted_sales_prices = sorted(sale_prices)
num_of_sales = len(sorted_sales_prices)
first_sales_items = sorted_sales_prices[:math.floor(num_of_sales/2)] # first slice to grab first four elements (floor takes 4.5 and provides 4 since floor rounds down)
last_sales_items = sorted_sales_prices[:-(math.floor(num_of_sales/2)):] # gets last four .... last : brings us all the way to end
median = sorted_sales_prices[math.floor(num_of_sales/2):(math.floor(num_of_sales/2) + 1)]

print(sorted_sales_prices) # prints sorted() list
print(num_of_sales) # prints 9
print(first_sales_items) # prints [1, 3, 10, 40]
print(last_sales_items) # prints [100, 100, 220, 400]
print(median) # prints [83]
# code perspective this is very ugly bad practice with duplicate code
