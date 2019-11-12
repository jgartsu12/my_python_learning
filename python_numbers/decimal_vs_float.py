from decimal import Decimal # import decimal python library # take Decimal class from decimal library

product_cost = Decimal(88.40) # python decimals
commission_rate = Decimal(0.08)
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty) # prints 42962.40000000000282883716451 
# decimals give u higher level of precision 