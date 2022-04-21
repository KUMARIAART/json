"Python object ko json string mai convert karne ka program likho?"

import json

dict={
    "name": "David", 
    "class": "I", 
    "age": 6
}
print(type(dict))
json_data=json.dumps(dict)
print(json_data)

