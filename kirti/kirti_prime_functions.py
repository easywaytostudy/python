print("####################################  P r i m e		N u m b e r s  #####################################")
print("_________________________________________________________________________________________________________")
print("")
print("")
print("")
print("First is to check that number is prime or not.!!!")
print("_________________________________________________")
print("")
def primeornot(x):
	c=x
	if c<2:
		print("x = ",c," is not a prime number.!")
	if x==2:
		print("x = ",c," is a prime number.!")
	else:
		for i in range (2,c):
			if c%i==0:
				print("x = ",c," is not a prime number.!")
				break
			if c%i!=0 and i+1==c:
				print("x = ",c," is a prime number.!")
				

x=input("Enter a number to check that it's prime or not - ")
primeornot(int(x))

print("")
print("")
print("")
print("Now in second program we try to print all prime numbers in between given range.!!!")
print("__________________________________________________________________________________")
print("")
def printprimenumbers(a,b):
	for i in range (a,b+1):
		if i==2:
			print (i)
		if i>2:
			for j in range (2,i):
				if i%j==0:
					break
				if i%j!=0 and j+1==i:
					print (i)

print("Enter the range in which you want to print the prime numbers")
a=input("Enter starting integer of range - ")
b=input("Enter ending integer of the range - ")
printprimenumbers(int(a),int(b))

print("")
print("____________________________________________________________________________________")						
						
						


	
