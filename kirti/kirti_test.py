print("kirti deshwal 4th feb test answers")
print("#################### Program 2 (Factorial) ######################")
x=input("Enter a number for which you want to find factorial - ")
x=int(x)
fact=x
for i in range(1,x):
	fact=fact*i
print("factorial of the given number is ",fact)
print("____________________________________________________________________________")
print("")
print("#################### program 3 ######################")
x=input("Enter any number - ")
x=int(x)
data={}
for i in range(1,x+1):
	data[i]=i*i
print(data)	
print("____________________________________________________________________________")
print("")
print("#################### Program 5.1 (Palindrome) ######################")
x=input("Enter any number - ")
x=int(x)
n=x
r=0	
while n>0:
	a=n%10
	r=r*10+a
	n=n//10
if r==x:
	print(x," is Palindome.")
else:
	print(x," is not Palindrome.")
print("____________________________________________________________________________")
print("")
print("#################### Program 5.2 (Armstrome) ######################")			
x=input("Enter any number - ")
x=int(x)
n=x
z=x
c=0
while n>0:
	c=c+1
	n=n//10
r=0	
while z>0:
	a=z%10
	r=r + a**c
	z=z//10
if r==x:
	print(x," is Armstrome.")
else:
	print(x," is not Armstrome.")
print("____________________________________________________________________________")
print("")
print("#################### Program 5.3 (Reverse) ######################")
x=input("Enter any number - ")
x=int(x)
n=x
r=0	
while n>0:
	a=n%10
	r=r*10+a
	n=n//10
print("Reverse of ",x," is ",r)
print("____________________________________________________________________________")
print("")
print("#################### Program 5.4 (Even-Odd) ######################")
x=input("Enter any number - ")
x=int(x)
if x%2==0:
	print(x," is even number.")
else:
	print(x," is odd number.")
print("____________________________________________________________________________")
print("")
print("#################### Program 5.5 (Prime number) ######################")
x=input("Enter any number - ")
x=int(x)		
if c<2:
	print(x," is not a prime number.!")
if x==2:
	print(x," is a prime number.!")
else:
	for i in range (2,x):
		if x%i==0:
			print(x," is not a prime number.!")
			break
		if x%i!=0 and i+1==x:
			print(x," is a prime number.!")
print("____________________________________________________________________________")
print("")
print("#################### Program 5.6 (Leap year) ######################")
x=input("Enter any number - ")
x=int(x)					
if x%4==0:
	print(x," is a leap year.")
else:
	print(x," is not a leap year.")	
print("____________________________________________________________________________")
print("")
print("#################### Program 6 (Patterns) ######################")
print ('First Triangle')
print ('')
for i in range (1,6):
	print (i*"*")

print ("")
print ('Second Trinangle')
print ('')
for i in range (5,0,-1):
	print (i*"*")

print ('')
print ('Third Triangle')
print ('')
for i in range (1,6):
	print ((5-i)*" ",i*"*")

print ('')
print ('Fourth Triangle')
print ('')
for i in range (1,6):
	print ((i-1)*" ",(6-i)*"*")
print("____________________________________________________________________________")
print("")
print("#################### Program 6 (Patterns) ######################")
print("")
res =[
	{'id': 62, 'first_name': 'Test', 'last_name': 'Test', 'email': 'test@gmail.com', 'dog_id': 246, 'name': 'rrg', 'sex': 'f', 'age_months': 95, 'birth_month': 12, 'birth_day': 6, 'feeding_amount_kcal': 1741.4, 'feeding_amount_cups': 3.0},
	{'id': 62, 'first_name': 'Test', 'last_name': 'Test', 'email': 'test@gmail.com', 'dog_id': 248, 'name': 'iu', 'sex': 'm', 'age_months': 80, 'birth_month': 10, 'birth_day': 7, 'feeding_amount_kcal': 1834.2, 'feeding_amount_cups': 3.0},
	{'id': 62, 'first_name': 'Test', 'last_name': 'Test', 'email': 'test@gmail.com', 'dog_id': 249, 'name': 'b fgbg', 'sex': 'm', 'age_months': 82, 'birth_month': 12, 'birth_day': 5, 'feeding_amount_kcal': 1628.1, 'feeding_amount_cups': 3.0},
	{'id': 62, 'first_name': 'Test', 'last_name': 'Test', 'email': 'test@gmail.com', 'dog_id': 261, 'name': 'njfrnf', 'sex': 'm', 'age_months': 200, 'birth_month': 4, 'birth_day': 13, 'feeding_amount_kcal': 1467.3, 'feeding_amount_cups': 3.0},
	{'id': 63, 'first_name': 'Dave', 'last_name': 'Knoepfle', 'email': 'dave.knoepfle@coastandrange.com', 'dog_id': 250, 'name': 'Dharma', 'sex': 'f', 'age_months': 125, 'birth_month': 5, 'birth_day': 31, 'feeding_amount_kcal': 1101.2, 'feeding_amount_cups': 2.0},
	{'id': 63, 'first_name': 'Dave', 'last_name': 'Knoepfle', 'email': 'dave.knoepfle@coastandrange.com', 'dog_id': 251, 'name': 'Hana', 'sex': 'f', 'age_months': 116, 'birth_month': 2, 'birth_day': 14, 'feeding_amount_kcal': 1560.3, 'feeding_amount_cups': 3.0},
	{'id': 63, 'first_name': 'Dave', 'last_name': 'Knoepfle', 'email': 'dave.knoepfle@coastandrange.com', 'dog_id': 252, 'name': 'Hana', 'sex': 'f', 'age_months': 116, 'birth_month': 2, 'birth_day': 14, 'feeding_amount_kcal': 845.2, 'feeding_amount_cups': 1.0},
	{'id': 63, 'first_name': 'Dave', 'last_name': 'Knoepfle', 'email': 'dave.knoepfle@coastandrange.com', 'dog_id': 254, 'name': 'Dharma', 'sex': 'f', 'age_months': 53, 'birth_month': 4, 'birth_day': 4, 'feeding_amount_kcal': 1483.6, 'feeding_amount_cups': 3.0},
	{'id': 64, 'first_name': 'Leith', 'last_name': 'Henry', 'email': 'konaskitchen@gmail.com', 'dog_id': 253, 'name': 'Hana', 'sex': 'f', 'age_months': 117, 'birth_month': 2, 'birth_day': 14, 'feeding_amount_kcal': 845.2, 'feeding_amount_cups': 1.0},
	{'id': 65, 'first_name': 'Becky', 'last_name': 'Knoepfle', 'email': 'rebeccaknoepfle@hotmail.com', 'dog_id': 255, 'name': 'Dharma', 'sex': 'f', 'age_months': 124, 'birth_month': 5, 'birth_day': 31, 'feeding_amount_kcal': 1175.5, 'feeding_amount_cups': 2.0},
	{'id': 66, 'first_name': 'Tenicka', 'last_name': 'Kingsley', 'email': 'tenicka_kingsley@yahoo.com', 'dog_id': 256, 'name': 'Nala', 'sex': 'f', 'age_months': 51, 'birth_month': 8, 'birth_day': 1, 'feeding_amount_kcal': 510.2, 'feeding_amount_cups': 1.0},
	{'id': 66, 'first_name': 'Tenicka', 'last_name': 'Kingsley', 'email': 'tenicka_kingsley@yahoo.com', 'dog_id': 257, 'name': 'Nala', 'sex': 'f', 'age_months': 51, 'birth_month': 8, 'birth_day': 1, 'feeding_amount_kcal': 510.2, 'feeding_amount_cups': 1.0},
	{'id': 66, 'first_name': 'Tenicka', 'last_name': 'Kingsley', 'email': 'tenicka_kingsley@yahoo.com', 'dog_id': 258, 'name': 'Nala', 'sex': 'f', 'age_months': 51, 'birth_month': 8, 'birth_day': 1, 'feeding_amount_kcal': 510.2, 'feeding_amount_cups': 1.0},
	{'id': 67, 'first_name': 'Priyanka', 'last_name': 'Superstar', 'email': 'priyanka.impinge@gmail.com', 'dog_id': 259, 'name': 'Doug', 'sex': 'f', 'age_months': 68, 'birth_month': 4, 'birth_day': 8, 'feeding_amount_kcal': 980.8, 'feeding_amount_cups': 2.0},
	{'id': 68, 'first_name': 'Gggfg', 'last_name': 'Ggju', 'email': 'tesrgg@ftj.hhj', 'dog_id': 260, 'name': 'Thhj', 'sex': 'm', 'age_months': 28, 'birth_month': 5, 'birth_day': 4, 'feeding_amount_kcal': 879.1, 'feeding_amount_cups': 1.0}
]


c=0
for j in res:	
	dogs=[]
	g=j['id']
	if c!=g:
		for i in res:
			c=g
			if i['id']==g:
				x={'Name':i['name']}
				y={i['dog_id']:x}
				dogs.append(y)
				dog={'email':i['email'],'dogs':dogs}
				id={i['id']:dog}				
		print(id)	

