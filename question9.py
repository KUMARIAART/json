"Apki pass ek shopping name ki ek dictionary hai"
{
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
"Apki dictionary ka use kar ke ek json file create karna hai."
"Aur apko kuch task perform karne hai jaise ki"

"1 main dekhna chahta hu shopping list ko json file dekhna."
"2 phir main user se poochu ga ki kon sa item khareedna chahte ho."
"3 uske baad user name dega phir user se input poochege jaise ki tum kitne item chahte ho."
"4 phir aapka wo number of items json file se remove karna hai."
"5 Agar tumhe shopping items add karna hai to tumko json file main insert karna hoga."

import json
dict={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
ask=input("What you want to add/A and remove/R :- ")
if ask=="R":
    item=input("enter iteam name:-")
    quantity=int(input("enter any number:-"))
    for i in dict:
        for j in dict[i]:
            if item==j:
                s=int(dict[i][j])
                if quantity<=s:
                    dict[i][j]=str(s-quantity)
                else:
                    print("we dont have much a stock")         
elif ask=="A":
    item=input("enter iteam name:-")
    quantity=int(input("enter any number:-"))
    for i in dict:
        dict[i][item] =str(quantity)
else:
    print("start from begining")
    

jsonfile=open("shopinglist.json","w")
json.dump(dict,jsonfile,indent=4)
jsonfile=open("shopinglist.json","r")
y=json.load(jsonfile)
print(y)
jsonfile.close()