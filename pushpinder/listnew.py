rick=["hello","bye",1,2,4]
print(rick)
rick.append("hi")	#first
print("after append", rick)

rick.clear() 			#second
print("the data of list get deleted",rick)

list=[1,2,3,"good","bad",1]
print(list)
print(list[4])		# to print the 4th index value
print(list[-1])		# to print the last value of list

x=list.copy()
print("after copy",x)			#3rd

print(list.count(1))			#4th


b=[1,2,37,6,5]
print("First list",list)
print("second List",b)			#5
print(list.extend(b))
print("after combine",b)

print(list.index("good"))		#6

list.insert(2,"bye")		#7
print(list)

print("Before pop",list)
list.pop(1)
print("After pop",list)		#8

print("list before remove",list)		#9
list.remove(1)

print(list)
list.reverse()			#10
print(list)

d=[1,2,6,7,9]
d.sort()			#11
print(d)