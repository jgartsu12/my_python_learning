# Overview of While Loops in Python
# key diff btwn for/in and while loops:
''' 
for/in loops: clear start and end - knows whn to stop

while loops: will not stop when u reach end of list --- while loops need to know when to stop
        # if not stopped = infinite loop crash ur program 
        # centinal value --> tells while loop when to stop
'''

# nums = list(range(1, 100))

# print(nums)

''' => 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78,
79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97,
98, 99] 
'''

# nums = list(range(1, 100))

# for num in nums:
#     print(num)
''' => 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
'''

# nums = list(range(1, 100))

# while len(nums) > 0: # while the length of the nums list is greater than 0
#     print(nums.pop()) # iterate over list and pop off and return that value and remove that item from the nums list to create the sentinel** value once 0 is reach to stop the loop (when false)
# ''' => goes from 99 to 1 ending 
# 99
# 98
# 97
# 96
# 95
# 94
# 93
# 92
# 91
# 90
# 89
# 88
# 87
# 86
# 85
# 84
# 83
# 82
# 81
# 80
# 79
# 78
# 77
# 76
# 75
# 74
# 73
# 72
# 71
# 70
# 69
# 68
# 67
# 66
# 65
# 64
# 63
# 62
# 61
# 60
# 59
# 58
# 57
# 56
# 55
# 54
# 53
# 52
# 51
# 50
# 49
# 48
# 47
# 46
# 45
# 44
# 43
# 42
# 41
# 40
# 39
# 38
# 37
# 36
# 35
# 34
# 33
# 32
# 31
# 30
# 29
# 28
# 27
# 26
# 25
# 24
# 23
# 22
# 21
# 20
# 19
# 18
# 17
# 16
# 15
# 14
# 13
# 12
# 11
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# '''
# # build guessing game with function and while loop - use when u dont know how many times u want program to iterate through collection
def guessing_game(): # user guesses until right answer is guessed
    while True:
        print('What is your guess?')
        guess = input()    # sets up prompt into terminal and store what evers written into it

        if guess == '42':
            print('You guess correctly')
            return False # continues to be true until told it is false ==> SENTINEL value to stop while loop
        else:
            print(f'No, {guess} is not correct, please try again\n') # \n gives new line so user can guess on new line

guessing_game() 
''' =>

What is your guess?
2
No, 2 is not correct, please try again

What is your guess?
1
No, 1 is not correct, please try again
What is your guess?
53
No, 53 is not correct, please try again

What is your guess?
42
You guess correctly
'''