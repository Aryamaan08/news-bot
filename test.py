import json

f = open('test.json', 'w')
json.dump({'a': 'b', 'c': 'd'}, f)
