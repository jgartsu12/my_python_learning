# Overview of Python List Query Processes: len(), Negative Indexes, and index()

# length fn = len() - count of elements in a list .. inside ur query ?
tags = ['python', ' development', 'tutorials', 'code']

number_of_tags = len(tags)

print(number_of_tags) 

# len() vs index() 
    # 4 elements are inside but the it still starts with index 0 so last index value in this list is 3 not four == error: off-by 1-error