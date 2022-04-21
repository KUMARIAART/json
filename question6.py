"Python object key unique key value ko access karne ka program likho?"

import json 

python_object='{"a":1,"a":2,"a":3,"a":4, "b":1, "b":2}'
print(python_object)
print(type(python_object))
unic_key=json.loads(python_object)
print(unic_key)
print(type(unic_key))









