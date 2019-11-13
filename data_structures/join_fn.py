# Using the join Function in Python to Build a URL Query String
        # https://www.google.com/search?q=python+development+tutorial  --> search string google uses to get ur result set (replicate this process)
# joins = str based fn ; need to tell it deliminator charac whihc will be a +
uri = 'https://www.google.com/search?q='
tags = ['python', 'development', 'tutorial'] # search terms
formatted_tags = '+'.join(tags) # join all tags together with deliminator which will be a +

print(formatted_tags) # prints python+development+tutorial