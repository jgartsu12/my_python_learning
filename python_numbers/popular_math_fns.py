import math 

loss = -20.25
product_cost = 89.99
# find abs value and wanted floor of loss
print(abs(math.floor(loss))) #nested fns
# prints 21 because math.floor() is being called before abs() thus providing wrong value wanted

print(math.floor(loss)) # prints -21  # give opposite as it was a positive value --> priority works with PEMDAS
