#/usr/bin/python3

from xwikiclient import Client
import json

client = Client()

result = client.spaces()
print (json.dumps(result, sort_keys = True, indent = 4))

result = client.space_names()
print (result)
