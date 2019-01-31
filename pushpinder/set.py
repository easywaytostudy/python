
print("...................SET Function.................")
set1={"hello","rick",1,5,3}
print(set1)

print(dict(name='gaurav', age=25))
for x in set1:
	print(x)
print(".........................")

print("rick" in set1)
print(".........................")

set1.add("world")
print(set1)
print(".........................")

set1.update(["hii",3,6,9])
print(set1)
print(".........................")

print(len(set1))
print(".........................")

set1.remove("hii")
print(set1)
print(".........................")

set1.pop()
print(set1)
print(".........................")

list1=("happy",1,3,5,1,1)
print(list1)
list2=set(list1)
print(list2)
print(".........................")

print("........difference..........")
x=set1.difference(list2)
print(x)

print("............intersection.........")
x=set1.intersection(list1)
print(x)

print("..............isdisjoint.........")
x=set1.isdisjoint(list1)
print(x)

print(".............issubset..........")
x=set1.issubset(list1)
print(x)

print("............issuperset..........")
x=set1.issubset(list1)
print(x)

print("..........symmetric difference..........")
x=set1.symmetric_difference(list1)
print(x)

print("........union........")
x=set1.union(list1)
print(x)
