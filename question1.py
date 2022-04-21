"Json data ko python object main convert karne ka program likho?."

import json

dict1='{ "name":"John", "age":30, "city":"New York"}'
dict2=json.loads(dict1)
print(dict2)
print(dict2["age"])
print(type(dict2))

