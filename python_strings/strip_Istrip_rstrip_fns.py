# Overview of Python's strip, lstrip (L strip), and rstrip Functions
url = '     https://google.com      '

# using L - strip => Left strip
url = url.lstrip('htts://')
#r strip
url = url.rstrip('.com')
url = url.capitalize()

print(url) # prints out just Google
# machine alg clean up - get data and format it properly (used often) since dealign with raw data