# Build a Histogram in Python with No 3rd Party Libraries
# histogram --> used in stats and machine lerning to see patterns and basic types of trends w/ data
#  number and strings are different data types so u cant combine u will get a TypeError
        # in console if u type > 4 * 'w' => returns this string 'wwww'
""" sale count = $... g= google... f = facebook... t = twitter ... o =offline
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""

sales = {
    'google': 20,
    'facebook': 42,
    'twitter': 10,
    'offline': 12,
} 
# older form of str interpolation could use bracket syntax if u want

print('g ' + sales['google'] * '$') # combine a string with an integer so need to do multiplication 
    # returns g $$$$$$$$$$$$$$$$$$$$

print('f ' + sales['facebook'] * '$') # returns f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


print('g ' + sales['twitter'] * '$') # => t $$$$$$$$$$


print('o ' + sales['offline'] * '$') # => o $$$$$$$$$$$$
