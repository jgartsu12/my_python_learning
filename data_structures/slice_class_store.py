tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

# how to retrieve result set from slice class --> BEHIND THE SCENES
slice_obj =slice(2)  # difference between this and print(tags[:2]) ==> can store it inside object and call it anywhere in the program allows u store ur slice
# just doing --> slice_obj = [:2] returns SyntaxError 

print(tags[slice_obj]) # --> this retrieves ['python', 'development'] result set previously obtained in print(slice_obj)