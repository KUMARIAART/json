"Python object ko json data main convert karne ka program likho?"

import json
x={
    "name": "David", 
    "class": "I", 
    "age": 6,
    "num":True
}
y=json.dumps(x)
print(y)
# print(type(y))
# print(y["age"])

