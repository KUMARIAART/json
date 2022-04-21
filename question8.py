"Tumhare pass four employes ki details hai list mai:-"

# [["neelam","programer","24","2400"],
#         ["komal","trainer","24","20000"],
#         ["anuradha","HR","25","40000"],
#         ["Abhishek","manager","29","63000"]]

"ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4."
"har ek employee ka dictionary main name,designation,age and salary honi chahiye."
"aur ye sab dictionary ki keys hai jismai maine list main value di hai. Iska use kar ke aapko ek "
"json file create karni hai? Jaise ki niche diya hai."

import json

list=[["neelam","programer","24","2400"],
        ["komal","trainer","24","20000"],
        ["anuradha","HR","25","40000"],
        ["Abhishek","manager","29","63000"],
        ["sheetal","student","18","0000"],
        ["aarti","developer","23","50000"]]
dic={}
i=0
while(i<len(list)):
    d={}
    main_key=input("Enter the main key:-")
    d["Name"]=list[i][0]
    d["Designation"]=list[i][1]
    d["age"]=list[i][2]
    d["salary"]=list[i][3]
    dic[main_key]=d
    i+=1

jsonfile=open("employfile.json","w")
json.dump(dic,jsonfile,indent=4)
jsonfile.close()
jsonfile=open("employfile.json","r")
y=json.load(jsonfile)
print(y)







