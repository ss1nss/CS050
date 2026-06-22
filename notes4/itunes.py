# API = application program interface; you can access database/ server to access it from your own database/server
# APIs can be installed with the "pip install requests", which you then can link to your HTTP/S
# JSON = java script notation; language agnostic = meaning you can use other coding languages like python to read these files

#import requests
#import sys

#if len(sys.argv) != 2:
#    sys.exit()

#response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]) # setting response as the variable for whatever info you are getting from the server
#print(response.json()) # if you run the program + a name of a band, you will get a bunch of notated data/ dictionary

import json # this will prettily print the json notation into a more readable format; there's another library you can import called json, that will make these api data look pretty :3
import requests
import sys

if len(sys.argv) != 2:
    sys.exit() # sys.exit terminates the program, break, for now, only for loops

#response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]) # the entire string in the website is editable, for instance changing the limit will provide more items
#print(json.dumps(response.json(), indent=2)) # this will print the entire response, but "prettier" :3

#o = response.json()
#for result in o["results"]:
#    print(result["trackName"]) # to print out just the 1 thing you want within the API

# there can be dictionaires within dictionaries indicated by curly braces {}
# like a dictionary on dogs, then further separating by color and type, then giving further dictionaries for color and type

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o = response.json()
for result in o["result"]:
    print(result["rate"])
