# Overview of Python Conditionals
# if conditional:
# age = 25

# if age < 25:
#     print(f"I'm sorry you need to be atleast 25 years old") # nothing happens becuase age was 25 ... condition is False

# age = 15

# if age < 25:
#     print(f"I'm sorry you need to be atleast 25 years old") # return statement because 15 < 25 since condition is True

# if/else 
# age = 1500

# if age < 25:
#     print(f"I'm sorry you need to be at least 25 years old") # if true
# else: # if false
#     print(f"You're good to go, {age} fits in the range to rent a car")
#     # => You're good to go, 1500 fits in the range to rent a car
#     # thus prints a statment always whether True or False

# if/elif/else (ELIF = ELSE IF)
age = 120

if age < 25:
  print(f"I'm sorry, {age} is under 25 years old") # TOO YOUNG TO RENT CAR
elif age > 100:
  print(f"I'm sorry, {age} is over 100 years old") # TOO OLD TO RENT CAR
else: # BOTH ITEMS ABOVE ARE FALSE
  print(f"You're good to go, {age} fits in the range to rent a car") # JUST RIGHT TO RENT A CAR

  # RETURNS =>  I'm sorry, 120 is over 100 years old