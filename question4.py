"Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?"

import json

dic={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}	

x=json.dumps(dic, indent=1, sort_keys=True) 
print(x) 
  



 



