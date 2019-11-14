# Working with the slice Class in Python to Store Slices

tags = [
  'python',  # index =  0
  'development',   #    1
  'tutorials', #        2
  'code', #             3
  'programming', #      4
]

#used in machine learning and data science
# [starting point index : ending point index : step point/interval index]
print(tags[1:4:2]) # returns --> ['development', 'code'] --> same as below print statement 

slice_obj = slice(1:4:2)  
# an alg may return a slice but u may not know the start or stop pts are
#helper fns with slice class --> [start , stop, index] --> production application
print(slice_obj.start) # --> returns starting index to see where it started which is 1
print(slice_obj.stop) # --> returns ending index point to see when it stopped which is 4
print(slice_obj.step) # --> returns the step --> interval which is 2
print(tags[slice_obj]) 

