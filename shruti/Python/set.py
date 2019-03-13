### set commands
thisset = {"apple","banana","cherry"}
print(thisset)

### access items
for x in thisset:
	print(x)

### add items
thisset.add("orange")

### update()
thisset.update(["mango","grapes","papaya"])

### len()
print(len(thisset))

### remove()
thisset.remove("cherry")

	##OR##

### discard()
thisset.discard("banana")

	##OR##

### pop()
thisset.pop()

### clear()
thisset.clear()

### del()
del thisset

### set()
thisset = set(("apple","mango","banana","cherry","peach","grapes"))

### copy()
x = thisset.copy()
print(x)

### difference()
y = {"google","microsoft","peach"}
z = x.difference(y)
print(z)

### intersection()
w = x.intersection(y)
print(w)

### disjoint()
z = x.isdisjoint(y)
print(z)

###  issubset()
z = x.issubset(y)
print(z)

### issuperset()
z = x.issuperset(y)
print(z)

### symmetric_difference()
z = x.symmetric_difference(y)
print(z)

### union()
z = x.union()
print(z)
