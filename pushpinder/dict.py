dict={"Hello":"Bye","Car":"Bike","Day":"Night","Slow":"Fast"}
print(dict)

print(dict["Hello"])   #to check the corresponding value

dict["Car"]="Audi"
print(dict)           # to change the value 

for x in dict:
	print(x)		# to print all the key values of dictonary

for x in dict:
	print(dict[x])		#to print all the value terms 

for x, y in dict.items():
	print(x,y)			# to print all the values and keys of dictonry

if "Car" in dict:
	print("yes it exsits")  # to check the item through if statement
else:
	print ("wrong data")

print(len(dict))

dict["Fat"]="Slim"
print(dict)

print("to add new")			#to add new item in dictonary

dict.pop("Day")
print(dict)			# to delete a element from dictonary

dict.popitem()	#it will delete the last element which is inserted in dictonary
print(dict)


dict.clear()		#clear the data of dictonary
print(dict)

