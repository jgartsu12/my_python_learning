# Guide to Python Lambdas
# lambda -> tool that allows u wrap a fn (usually smaller fn) and pass it to other fns
    # -> wrap beh and pass it to other fns (mobile fns)
    # -> wrap a process  (wrap functionalities)
    # -> return a value
# py fn -> first class citizens => can treat a fn like any other obj
# fn_name = lambda fn_args... : value returned

full_name = lambda first, last: f'{first} {last}'

print(full_name('J', 'Low')) # lambdas only return a value so print() needed
                # => prints J Low

def greeting(name):
    print(f'Hi there {name}')


greeting(full_name('tiffany', 'H')) # first goes to lambda and pass in thse values and then lambda procesees and then it is stored in full_name variable which is then passed into greeting fn
# => Hi there tiffany H