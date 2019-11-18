import sys # directly in py lang
sys.path.insert(0, './libs') # look into working directly to find libs
import helper

def render():
    print(helper.greeting('T', 'hhh'))


render()
