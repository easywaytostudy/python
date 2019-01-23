print ('                        PYTHON DICTIONARY                             ')
print(' --------------------------------------------------------------------------')
print(' ')
dict={'name':'arti',
'age':21}
print(dict)
print(' ')
print(' --------------------------------------------------------------------------')
print('accessing a particular item from dictionary')
x=dict['age']
print(x)
print(' ')
print('                   OR                         ')
print(' ')
print('accessing a item using get()')
x=dict.get('age')
print(x)
print(' --------------------------------------------------------------------------')
print('changing the values from the dictionary....from 21 to 22 ')
dict['age']=22
print(dict)
print(' ')
print(' --------------------------------------------------------------------------')
print('showing the keys using for loop')
for i in dict:
	print(i)
print(' ')
print(' --------------------------------------------------------------------------')

print('showing the values of the dictionary')
for i in dict:
	print(dict[i])
print('                   OR                         ')
print(' ')
print('showing the values using values()')
for i in dict.values():
	print(i)
print(' ')
print(' --------------------------------------------------------------------------')
print('showing both keys and values using loop')
for x,y in dict.items():
	print(x,y)
print(' ')
print(' --------------------------------------------------------------------------')
print('to check whether the key is present in the dictionary or not')
if 'name' in dict:
	print("Yes, 'name' is one of the keys in the dict dictionary")
print(' ')
print(' --------------------------------------------------------------------------')
print('length of the dictionary')
print(len(dict))
print(' ')
print(' --------------------------------------------------------------------------')
print('adding items')
dict['place']='ambala'
print(dict)
print(' ')
print(' --------------------------------------------------------------------------')
print('removing items using pop')
dict.pop('place')
print(dict)
print(' ')
print(' --------------------------------------------------------------------------')

# note that keywords are not string literals
# note the use of equals rather than colon for the assignment

print('copying the dict')
x = dict.copy()
print(x)
print(' ')
print(' --------------------------------------------------------------------------')
'''x = ('key1', 'key2')
y = 0

dict = dicti.fromkeys(x, y)


print(dict)'''
print('showing the default value')
x = dict.setdefault('age', 35)
print(x)
print(' ')
print(' --------------------------------------------------------------------------')
dict.clear()
print (dict)
print(' ')
print(' --------------------------------------------------------------------------')



