imp@ubuntu:~$ python
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> list=["a","b","c",1,1,2,3,6]
>>> print list
['a', 'b', 'c', 1, 1, 2, 3, 6]
>>> list.index('c')
2
>>> list.append("l")
>>> print list
['a', 'b', 'c', 1, 1, 2, 3, 6, 'l']
>>> list2=["d","e"]
>>> print list2
['d', 'e']
>>> list.extend(list2)
>>> print list
['a', 'b', 'c', 1, 1, 2, 3, 6, 'l', 'd', 'e']
>>> list.insert(3,"h")
>>> print list
['a', 'b', 'c', 'h', 1, 1, 2, 3, 6, 'l', 'd', 'e']
>>> list.remove("l")
>>> print list
['a', 'b', 'c', 'h', 1, 1, 2, 3, 6, 'd', 'e']
>>> list.count(1)
2
>>> list.pop(3)
'h'
>>> print list
['a', 'b', 'c', 1, 1, 2, 3, 6, 'd', 'e']
>>> list.reverse()
>>> print list
['e', 'd', 6, 3, 2, 1, 1, 'c', 'b', 'a']
>>> list.sort()
>>> print list
[1, 1, 2, 3, 6, 'a', 'b', 'c', 'd', 'e']
>>> print(list[1])
1
>>> print list
[1, 1, 2, 3, 6, 'a', 'b', 'c', 'd', 'e']
>>> list[4]='u'
>>> print list
[1, 1, 2, 3, 'u', 'a', 'b', 'c', 'd', 'e']
>>> print list
[1, 1, 2, 3, 'u', 'a', 'b', 'c', 'd', 'e']
>>> if "u" in list:
...     print("yes,' 'u' is in the list ")
... 
yes,' 'u' is in the list 
>>> print (len(list))
10
 list=("a","b","c")
>>> print list
('a', 'b', 'c')
>>> print (list[1])
b
>>> print list
('a', 'b', 'c')
>>> for x in list:
...     print(x)
... 
a
b
c
>>> if "a" in list:
...     print("yes,'a' in the list")
... 
yes,'a' in the list
>>> print(len(list))
3
>>> del list
>>> print list
<type 'list'>
>>> print (list)
<type 'list'>
