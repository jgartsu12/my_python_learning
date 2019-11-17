# How to Combine and Flatten Lists in Python with the For / In Loop
# merge multiple lists with for/in loop

legacy_customers = ['Alice','Bob']
new_customers = ['Tiffany', 'Kristine']  

raw_db = [legacy_customers, new_customers] # created list with 2 lists -- trreated like 2 elemets

print(raw_db) # => [['Alice','Bob'], ['Tiffany', 'Kristine']]

for legacy_customer in legacy_customers:  # use for/in to iterate over legacy_customers and append add on it
    new_customers.append(legacy_customer)

print(new_customers) # => ['Tiffany', 'Kristine', 'Alice', 'Bob'] 
# iterate over prexisiting list and treat like normal strings