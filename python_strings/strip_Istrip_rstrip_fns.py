# Overview of Python's strip, lstrip (L strip), and rstrip Functions
url = '     https://google.com      '

print(url.strip('https://'))

# using L - strip => Left strip
print(url.lstrip('htts://'))
    # pirnts google.com