# Advanced Techniques for Implementing Ranges and Slices in Python Lists
# ranges vs slices 
    # ranges usually used when working w/ strings but slices in lists (some used interchangably)
tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]
# how is slice method different from sort() ???
# key difference: 
       # slice - it just reversed the index value
       # sort() - it looks at alphabetical value and reversed that
# tag_range = tags[::-1]

 # print(tag_range) # prints ['computer science', 'programming', 'code', 'tutorials', 'development', 'python']

#sort method
tags.sort(reverse=True)
print(tags) # prints ['tutorials','python', 'programming', 'development', 'computer science', 'code']

# how sort method can be tricky
sorted_tags = tags.sort(reverse=True)
print(sorted_tags) # prints None ... python's view on IMMUTABILITY --> what u can and cannot change
                    # python is so careful with immutability to so sort returns nothing --> changed order of the tags and reverse them but it will not return that value 
                        # key -> sort fn goes in and changes tags and but does not store it as an operation in a variable due to immutablity
                            # give warning that u changed an entire sort of elements to tell u tags list was effected
                            