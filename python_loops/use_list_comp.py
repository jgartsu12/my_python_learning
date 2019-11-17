# Introduction to Using List Comprehension in Python
# advanced concepts ~~ 
# list comp => can set up number of for in loops to function on single line to generate lists
    # works by understanding alternative
    # set of for/in loops and conditonals that can be placed in single line of code

num_list =range(1, 11)  # set cube numbers to **3 power returns a list of elements with cubed numbers
# cubed_nums = [] 

#traditional method vs list comp method
# traditional method
# for num in num_list:
#   cubed_nums.append(num ** 3)

# print(list(num_list)) # => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# print(cubed_nums)
# returns : [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]   == the cubed numbers in num_list

# how to use list comp method
# do not need to store in cubed_nums = [ ]
# base case
# cubed_nums = [num ** 3 for num in num_list]        # typically store it in [ ] --> dynamically generate list
#                 # num ** 3 action wanted
#                         # num could be anything like x ** 3 for x in num_list
#                 # for/in loop expression
#                     #for num in num_list
#                 # [] = tells python u want to dynnamixally generate a list in var called cubed_nums
# print(list(num_list)) # returns same as above
# print(cubed_nums)       # returns same as abobe
#~~~~~~~~~~~~~~ ~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# dynamically select items in a list generated
# list that captures even numbers between 1 and 11 excluding 11
# traditional method
num_list =range(1, 11)
even_numbers = []

for num in num_list:
    if num % 2 == 0: # is it even
        even_numbers.append(num)

print(list(num_list))
print(even_numbers)
  ''' => 
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (num_list)
    [2, 4, 6, 8, 10] (even_numbers)
    '''

# list comp method
even_numbers = [num for num in num_list if num % 2 == 0]
                # variable even_numbers that stores the list wrapper
                # no append needed since not starting with empty list .. generateed it on the fly
                # add num to even numbers if condition is met if even (condition) ..> if num % 2 == 0
                # traditional for in loop

print(list(num_list))
print(even_numbers) 
# returns same as the traditional approach
