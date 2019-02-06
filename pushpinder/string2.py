a="hello World"     
b="Good Morning"

print(a,b)
x=a.capitalize 	#First method       
print(a)

y=b.casefold()  #second method
print(b)

x=a.center(30)	#third method
print(x)		

y=b.count('o')  # 4th 
print(y)

x=a.encode()   #5th
print(x)

b="good day"
y=b.endswith("g")  #6th
print(y)
y=b.endswith("day",5,8)
print(y)

c="h\te\tl\tl\to"  #7th 
y=c.expandtabs(2)
print(y)

b="good day"        #8th
y=b.find("da")        
print(y)

d="hello123"		#9th
x=d.isalnum()
print(x)

x=d.isspace()		#10
print(x)

a="abc"
b="123"
x=a.format()   #11
print(x)
x=b.format()
print(x)

x=a.index("b")		#12
print(x)

a="\u0030"
print(a.isdecimal())	#13

b="56"
print(b.isdigit())		#14

a="hello"
print(a.isalpha())		#15

print(a.isidentifier())	#16

print("isprintable()")
print(a.isprintable())	#17

print("istitle()")
print(a.istitle())	#18

a="hello"
print("isupper")
print(a.isupper()) #19

d="hello sir good morning"
print("join")
x="$".join(d)
print(x)		#20

a="hello"
print("ljust")
x=a.ljust(10)	#21
print(x,"yes sir")

b="BYE"
print("lower")	#22
print(b.lower())

b="    hi    "
print("lstrip")		#23
print(b.lstrip())

d="i have to work"
print("partition")	#25
print(d.partition("to"))

a="hello friends"
print("replace friends with sir")	#26
print(a.replace("friends","Sir"))

print("rfind")
print(a.rfind("ir"))		#27

print("rindex")
print(a.rindex("lo"))		#28

print("split")
print(a.split())		#29

a="good\nnight"
print("splitlines")
print(a.splitlines())	#30

'''b="hello friends"
print("startwith")
print(b.startwith("hello"))	'''	#31

d="HellO FriEnds"
print("swapcase")
print(d.swapcase())		#32

print("title")
print(b.title())	#33

print("upper")
print(b.upper())	#34


print("zfill")
print(a.zfill(20))	#35

b="Can I go to home"
print("rpartition")
print(b.rpartition("go"))	#36

b="he ,ll, o "
print("rsplit")
print(b.rsplit(","))	#37

b="bye"
print("maketrans")
print(b.maketrans("y","q"))	#38


