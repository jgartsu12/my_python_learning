# Overview of Python's strip, lstrip (L strip), and rstrip Functions
url = '     https://google.com      '

print(url.strip('https://')) # returns google.com  # error suspicous argument in strip call - dont want users to use these strip calls cuz they ccould inject something that could impact other data - security 