print('Python Dictionary:-Parvindet Singh')
print('---------------------------------------------------------------------')
dict={'name':'parvinder',
'age':22}
print(dict)
print('---------------------------------------------------------------------')
print('printing the particular item')
x=dict['age']
print(x)
print('same function using get keyword')
x=dict.get('age')
print(x)
print('---------------------------------------------------------------------')
print('changing the values from dictionary')
dict['age']=21
print(dict)
print('---------------------------------------------------------------------')
print('using for loop in dictionary showing the key')
for i in dict:
	print(i)
print('showing the values')
for x in dict:
	print(dict[x])
print('                    O R                ')
print('showing the values using value keyword')
for i in dict.values():

	print(i)
print('---------------------------------------------------------------------')
print('loop for both keys and values')
for x,y in dict.items():
	print(x,y)
print('---------------------------------------------------------------------')
print('checking using if statement')
if 'age' in dict:
	print('yes, age is in dictionary')
print('---------------------------------------------------------------------')
print('checking the length of the dictionary:-')
print(len(dict))
print('---------------------------------------------------------------------')
print('Adding items in dictionary')
dict['city']='mohali'
print(dict)
print('---------------------------------------------------------------------')
print('Removing items using pop:-')
dict.pop('age')
print(dict)
print('---------------------------------------------------------------------')
#dict1=dict(name='parvinder',age=22)
#print(dict1)
#print('---------------------------------------------------------------------')

print('using copy function')
x=dict.copy()
print(x)
print('---------------------------------------------------------------------')
print('returning the key using key keyword')
x=dict.keys()
print(x)
print('---------------------------------------------------------------------')
x=dict.setdefault('city','chd')
print(x)
print('---------------------------------------------------------------------')
print('Clearing the list')
dict.clear()
print(dict)
print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')
































