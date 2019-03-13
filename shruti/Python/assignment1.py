#list commands
list1 = ['Shruti','Dhiman',"Hello",1,3.5]

#access list items
print(list1[1])

#change item value
list1[1] = 'Anuj'
print("Modified List:",list1)

#loop through list items
for x in list1:
    print(x)

#to check if an item exists
if 'Hello' in list1:
    print("Yes")
else:
    print("No")

#copy()
list2 = list1.copy()
print("copied list",list2)

#len()
print("length of list:",len(list1))

#count()
print(list1.count(4))

#index()
print(list1.index("Hello"))

#append()
list1.append('Thapar')
print("list after adding an element:",list1)

#insert()
list1.insert(4,'Institute')
print(list1)


#remove()
list1.remove("Hello")
print("list after removing element:",list1)

#pop()
list1.pop()
print("list after pop operation:",list1)

#del()
del list1[1]
print(list1)

fruits = ['apple', 'banana', 'cherry']
#reversing list
fruits.reverse()
print("reversed list:",fruits)

#sort()
fruits.sort()
print("Sorted list:",fruits)

#sort in descending order
fruits.sort(reverse=True)
print(fruits)

#clear()
list1.clear()
print(list1)

#extend()
list3 = [5,6,7,8]
list3.extend(list2)
print(list3)


#tuple commands
tuple1 = ("Hello","I","am","SD")

#access elements
print(tuple1[1])

#looping through the tuple
for i in tuple1:
    print(i)

#modify tuple - cannot change the values

#check if item exists
if "I" in tuple1:
    print("yes")
else:
    print("no")

#tuple length
print("length of tuple:",len(tuple1))
    
#count()
print(tuple1.count("am"))

#index()
print(tuple1.index("Hello"))


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










