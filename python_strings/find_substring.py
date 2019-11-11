sentence = 'The quick brown fox jumped over the lazy dog.'
# in operator most prefered by py develops
query = 'oops' in sentence

print(query) # prints False

# find - index value where discovered first
# index - index value where discovered can cause program to stop if try to run and website breaks if user went to it 
# in operator - doesnt care about index value ... prefered to see if a value is in the string True or False in case u need to replace something .. does string contain this substring
    # in operator --> in conditionals:
if 'oops' in sentence:
    ... # cleaner code cuz less code
    # compared to unclean
if (sentence.finds('oops') != -1): 
    ... # less clean in conditionals will run into this but just showing u ... how to follow ind best practice --> USE In operator syntax
