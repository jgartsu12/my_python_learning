# How to Convert Between the Integer, Float, Decimal and Complex Numeric Data Types in Python
from decimal from Decimal 


product_cost = 88.40
commission_rate = 0.08
qty = 450

print(int(product_cost)) # prints 88  - keeps whatever int value is there
print(float(qty)) # prints 450.0
print(Decimal(product_cost)) # convert to decimal --> 88.799999999999999999999715...
print(complex(commission_rate)) # scientific prints (0.08+0j) - a complex obj