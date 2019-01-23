tuple=("hello","hi","bye",1,2,3,"hello")
print(tuple)
for i in tuple:
	print(i)

print("count")
print(tuple.count("hello"))	#1


print("index")
print(tuple.index("bye"))

print(len(tuple))