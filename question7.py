"Text file data ko json file data mai convert karo,jaise ki neeche diya hai?"

# Text.txt:-  
#  Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29
import json

text_file={"name":"abhishek",
"Designation":"CEO of navgurukul",
"gender":"male",
"age":"29"
}

out_file=open("jsondata.json","w")
json.dump(text_file,out_file,indent=7)
out_file.close()
out_file=open("jsondata.json","r")
y=json.load(out_file)
print(y)




