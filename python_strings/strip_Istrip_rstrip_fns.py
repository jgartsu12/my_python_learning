# Overview of Python's strip, lstrip (L strip), and rstrip Functions
url = '     https://google.com      '

# using L - strip => Left strip
url = url.lstrip('htts://')
#r strip
url = url.rstrip('.com')
url = url.capitalize()

print(url) # prints out just Google