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

tag_range = tags[:-1:2] # [::interval] --> take every other element from start up to last element

print(tag_range) # prints ['python','tutorials','programming']