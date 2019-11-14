tags = [
  'python',  # index
  'development',
  'tutorials',
  'code',
  'programming',
]
# explicit approach vs functional approach
print(tags[1:4:2]) # returns --> ['development', 'code'] --> same as below print statement 

slice_obj =slice(1:4:2)  # like tags[2:4:2]  --> skip every element between index 2 ending at the 4th index element
                        # with slice u could start with second element which has an index  of one to last element with index of 5

print(slice_obj) # returns slice(None, 2, None)
                        # explaination of these 3 arguments returned in slice:
                       
                        #       1. Start point
                        #       2. Step
                        #       3. End point 

print(tags[slice_obj]) # --> this retrieves ['python', 'development'] result set previously obtained in print(slice_obj)
                        # returns --> ['development', 'code'] which is the same as print(tags[1:4:2])

# an alg may return a slice but u may not know the start or stop
