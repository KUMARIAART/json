"Json string ko check karo ki bo complex object contain karti hai ya nahi?"

import json

dict1={"1":"aarti","2":"sonu","3":50+9j,"4":3-10j}
dict2=json.dumps(dict1)
print(type(dict2))
print(dict2)





