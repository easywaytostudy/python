print ("######################################	F u n c t i o n		T u t o r i a l  #######################################")

print("print 1 before and outside all method.!")

def Kirti(a, b, c):
	print("Inside Method Kirti!!!")
	if a>b and a>c:
		print("a = ",a," is the largest among all.")
	elif b>a and b>c:
		print("b = ",b," is the largest among all.")
	else:
		print("c = ",c," is the largest among all.")

print("print 2 after method 'Kirti' and also outside all methods.! ")

def Main():
	print("Inside Main Method!!!")
	a=input("Enter First Number - ")
	b=input("Enter Second Number - ")
	c=input("Enter Third Number - ")
	
	Kirti(a, b, c)

Main()


print("print 3 after all methods and outside all method.!")


