sentence = 'The quick brown fox jumped over the lazy dog.'
# index vs find method
query = sentence.find('oops')
query_two = sentence.index('oops')

print(query)
print(query_two) 
# prints error msg: Traceback (most recent call last):
 # File "find_substring.py", line 4, in <module>
    # query_two = sentence.index('oops')

