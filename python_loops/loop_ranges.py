# Guide to Looping Over Ranges in Python
# praactical when u know u have set number of times u want to loop through a data type but dont know much data
# for / in loop : for iterator var in range (arg1, arg2, arg3):
    # print(iterator_var)

# grab only elements u want to show this way 
for num in range(1, 10): 
    print(num) 
''' returns => 1-9
1   # range works same way u slice items in a range - 10 is the upperbound so it stops before 10 and ends at 9
2           # off-by-one error can print 
3
4
5
6
7
8
9
''' 
for num in range(1, 11): 
    print(num) # => prints numbers 1-10 

# for/in loop with third arg being the interval/step argument
for num in range(1, 11, 2): 
    print(num) 

''' returns  =>  2 = skip everyother number btween 1 and 11 exluding the upper bound 11
    1 
    3
    5
    7
    9
'''

for num in range(1, 11, 3): 
    print(num) # skips everything 3rd value between 1 and 11 excluding 11
""" =>
1
4
7
10
"""