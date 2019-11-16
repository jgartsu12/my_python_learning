# How to Use a Tuple as a Dictionary Key in Python

# multiple values in ea key 
# example ecom site to keep track of each package w/ metadata
# (weight, "name": [ids ...])
# data strucutre  with dictionary, tuple used as key, and a list as the value --> allows u to put metadata in
priority_index = {
    (1, 'premier'): [1, 34, 12],
    (1, 'mvp'): [84, 22, 24],
    (2, 'standard'): [93, 81, 3],
}

print(list(priority_index.keys())) # convert to lists so its now dict view => gives u abilit y to access these keys via traversal
            # => [(1, 'premier'), (1, 'mvp'), (2, 'standard')]
            # = featured packages 