# Various Methods for Merging Python Sets
# fns focused on how one set can work with another set
# how to guarantee  set uniquness
tags_one = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

tags_two = {
  'ruby',
  'coding',
  'tutorials',
  'development'
}

# Merged tags # very similar to a venn diagram
merged_tags = tags_one | tags_two
print(merged_tags) # returns elements from both sets besides the duplicate strings
########################
# tags in tags_ones but not in tags_two -- find tags only in tags_one set
#subtract these other items
exclusive_to_tag_one = tags_one - tags_two
print(exclusive_to_tag_one) # returns only {'python'}

# tags in tags_two but not in tags_one
exclusive_to_tag_two = tags_two - tags_one
print(exclusive_to_tag_two) # prints {'ruby', 'development'}

# tags found in both tags_one and tags_two
    # only shared items
universal_tags = tags_one & tags_two
print(universal_tags) # prints => {'coding','tutorials'}