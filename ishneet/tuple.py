>>> list1=tuple(("a","b","c"))
>>> print (list1)
('a', 'b', 'c')
>>> if "a" in list
>>>print("a" in list)
a in list
>>> list={"key":"value","key":"value"}
>>> print list
{'key': 'value'}
>>> list2={"fruit":"kiwi","season":"winter"}
>>> print (list2) 
{'season': 'winter', 'fruit': 'kiwi'}
>>> x=list2["fruit"]
>>> print(list2)
{'season': 'winter', 'fruit': 'kiwi'}
>>> print(x)
kiwi
>>> x=list2.get("fruit")
>>> print(x)
kiwi
>>> list2["season"]="summer"
>>> print list2
{'season': 'summer', 'fruit': 'kiwi'}
>>> for x in list2:
...     print x
... 
season
fruit
>>> for x in list2.values():
...     print(x)
... 
summer
kiwi
>>> for x,y in list2.items():
...     print(x,y)
... 
('season', 'summer')
('fruit', 'kiwi')
>>> print(len(list2))
2

