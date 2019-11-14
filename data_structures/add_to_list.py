# How to Add to a List in Python with Both In Place and Copy Processes
tags = ['python', 'development', 'tutorials', 'code']
# algorithms when iterating over a list makes u add elements to the list while looping through it
# key differences between In Place vs Copy

# wrong way to add to a list
tags[-1] = 'Programming'

tags.extend('programming') # returns --> ['python', 'development', 'tutorials', 'Programming'] # code got replaced with programming
                    # seems liked it worked BUTTTT --> ur not adding to list instead it got rid of the last element 'code' so it override it instead!!

#extend() --> take each string element and treated it as its own character -->
        # extend is only used to add to prexisting list
tags.extend('programming') # returned ==> ['python', 'development', 'tutorials', 'code', 'p','r', 'o', 'g', 'r', 'a', 'm', 'i', 'n', 'g']

# wrap string in ['str' ] to treat the str as a single element  # MOST COMMON PRACTICE ### could also wrap in data structure
tags.extend(['programming']) # --> returned : ['python', 'code', 'development', 'tutorials', 'Programming']

print(tags)

# trying to store in a new variable --> similar to sort() fn
new_tags = tags.extend(['programming'])

print(new_tags) # returns None --> extend changes tags in place but does not return a new value stored similar to sort() fn beh

# how can we store it in new variable

new_tags = tags + ['Programming']