# Using Python's replace Function to Find and Replace String Values
sentence = 'The quick brown fox jumped over the lazy dog'

sentence = sentence.replace('quick', 'slow')
# replace takes 2 arguments - 1st arg finds word looking for like quick; 2nd arg is word u want to replace 1st arg with
print(sentence)
# this prints: The slow brown fox jumped over the lazy dog || instead of : The quick~ brown fox jumped over the lazy dog