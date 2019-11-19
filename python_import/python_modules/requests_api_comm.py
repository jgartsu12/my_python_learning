# Overview of the Requests Package in Python to Communicate with APIs
# json - key value pairs
# requests package - communicate with app
# pprint => pretty print
# in terminal in py repl
import requests
import pprint

r = requests.get('https://api.dailysmarty.com/posts')
r.json()
pprint.pprint(r.json()['posts'][0])
pprint.pprint(r.json()['posts'][0]['url_for_post'])