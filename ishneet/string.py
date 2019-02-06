>>> txt="hello, and welcome"
>>> x=txt.capitalize()
>>> print x
Hello, and welcome
>>> x=txt.casefold()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'casefold'
>>> x=txt.center(20)
>>> print x
 hello, and welcome 
>>> x=txt.center(60)
>>> print x
                     hello, and welcome                     
>>> x=txt.count("hello")
>>> print x
1
>>> x=txt.count(txt)
>>> print x
1
>>> x=txt.encode()
>>> print x
hello, and welcome
>>> x=txt.encode()
>>> print()
()
>>> print(x)
hello, and welcome
>>> x=txt.endswith(".")
>>> print x
False
>>> x=txt.endswith("e")
>>> print x
True
>>> x=txt.expandtabs(2)
>>> print x
hello, and welcome
>>> x=txt.expandtabs(10)
>>> print x
hello, and welcome
>>> x=txt.index("welcome")
>>> print x
11
>>> x=txt.index("w")
>>> print x
11
>>> x=txt.index("co")
>>> print x
14
>>> x=txt.isalnum()
>>> print x
False
>>> x=txt.isalpha()
>>> print x
False
>>> txt1="8686"
>>> x=txt.isdigit()
>>> print x
False
>>> txt1="50800"
>>> x=txt.isdigit()
>>> print x
False
>>> x=txt1.isdigit()
>>> print x
True
>>> x=txt.islower()
>>> print x
True
>>> x=txt.isspace()
>>> print x
False
>>> x=txt.isupper()
>>> print x
False
>>> i=("a","b","c")
>>> x="#".join(i)
>>> print x
a#b#c
>>> x=txt.ljust(20)
>>> print x
hello, and welcome  
>>> x=txt.ljust(60)
>>> print x
hello, and welcome                                          
>>> x=txt.ljust(60)
>>> print (x,"to india")
('hello, and welcome                                          ', 'to india')
>>> x=txt.lstrip()
>>> t="orange"
>>> x=txt.lstrip()
>>> print("of all fruits",x, "is mine")
('of all fruits', 'hello, and welcome', 'is mine')
>>> x=t.lstrip()
>>> print("of all fruits",x, "is mine")
('of all fruits', 'orange', 'is mine')
