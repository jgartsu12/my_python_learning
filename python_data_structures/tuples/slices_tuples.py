# Guide to Slices in Python Tuples

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

print(post[:2]) # returns => tuple ('Python basics', 'Intro to guide to py') -> grab first 2 elements

print(post[1::2]) # => starts at second element and skips 'some cool content' and returns ==> ('Intro gudie to py', 'published')