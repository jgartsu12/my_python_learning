sentence = 'The quick brown fox jumped over the lazy dog.'
# index vs find method
query = sentence.find('oops')
# query_two = sentence.index('oops')

print(query) # prints -1 since find method cant find 'oops'; while index will print an error
# print(query_two) 


