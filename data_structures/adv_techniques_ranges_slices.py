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
# want to reverse all these index values: how - use slice tech
tag_range = tags[::-1] # flip entire order of the list

print(tag_range) # prints ['computer science', 'programming', 'code', 'tutorials', 'development', 'python']