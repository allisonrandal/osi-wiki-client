#/usr/bin/python3

from xwikiclient import Client
import json

client = Client('http://wiki.opensource.org/rest/wikis/xwiki/')

result = client.spaces()
print (json.dumps(result, sort_keys = True, indent = 4))

result = client.space_names()
print (result)
