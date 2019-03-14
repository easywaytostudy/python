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
