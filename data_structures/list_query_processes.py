# Overview of Python List Query Processes: len(), Negative Indexes, and index()

# length fn = len() - count of elements in a list .. inside ur query ?
tags = ['python', ' development', 'tutorials', 'code']

number_of_tags = len(tags)
# how can i grab w/o knowing the index?? 
last_item = tags[-1] # get last element by passing -1 to grab last element  to grab 'code' which is also index 3

print(number_of_tags) 
print(last_item) # prints code since it is the last item at index -1 or 3

