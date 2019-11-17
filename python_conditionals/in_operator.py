# How to Check if a Value is Included in a Python String or List
# ~~~ In Operator ~~


# sentence = 'The quick brown fox jumped over the lazy Dog'
# word = 'quick'

# if word in sentence:
#     print('The word was found in the sentence') # ==> returned
# else:
#     print('word not found in sentence')

# sentence = 'The quick brown fox jumped over the lazy Dog'
# word = 'dog'

# if word in sentence:
#     print('The word was found in the sentence') # ==> returned
# else:
#     print('word not found in sentence') # => returned because dog is spelled with capitol D

# sentence = 'The quick brown fox jumped over the lazy Dog'
# word = 'Dog'

# if word in sentence:
#     print('The word was found in the sentence') # ==> returned
# else:
#     print('word not found in sentence')

# in operator is case sense so can call lower() fn - case insensitive search
# sentence = 'The quick brown fox jumped over the lazy Dog'
# word = 'Quick'

# if word.lower() in sentence.lower():
#     print('The word was found in the sentence') # ==> returned
# else:
#     print('word not found in sentence')
# ~~~~~~~~~~~~~~~~  ~~~ ~~ ~~~ ~~~~ 
# In operator with collections of data:
# is this a member of this collection ? - how to say it
nums = [1, 2, 3, 4]

# if 3 in nums:
#     print('The number was found') # ==> returned
# else:
#     print('Number not found') 

if 5 in nums:
    print('The number was found') 
else:
    print('Number not found') # ==> returned