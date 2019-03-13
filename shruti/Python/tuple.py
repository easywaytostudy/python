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

