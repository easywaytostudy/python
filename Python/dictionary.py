#dictionary commands
dict1 = {
    "name" :"Shruti",
    "age" : 20,
    "college" :"Thapar",
    "home" : "himachal"
}
print("dictionary is:",dict1)

#copy()
dict2 = dict1.copy()
print("copied dict:",dict2)

#fromkeys()
new_dict = dict.fromkeys(dict1,dict2)
print("new dict:",new_dict)

print("access elements")

#access element
x = dict1["home"]

####OR#######
x=dict1.get("home")

dict1["age"]=19

#setdefault()
x=dict3.setdefault("name","Shreiya")
print(x)

#update()
dict2.update({"home":"Kangra"})
print("updated dictionary:",dict2)

#print all key names one by one
for x in dict1:
    print(x)
print("keys are:")
for x in dict1.keys():
    print(x)

#print all values one by one
for x in dict1:
    print(dict1[x])

print("Values are:")
for x in dict1.values():
    print(x)


#print both keys and values
for x,y in dict1.items():
    print(x,y)


#check if key exists
if "home" in dict1:
    print("yes")

#length of dict
print("length of dict is:",len(dict1))

#add items
dict1["place"]="kangra"
print(dict1)

#remove items
dict1.pop("age")
print(dict1)

#popitem() - removes last inserted item
dict1.popitem()
print(dict1)


#del() - removes item with specified key name  or can delete entire dict
del dict1["home"]
print(dict1)


#clear() - empties the dict
dict1.clear()
print(dict1)

