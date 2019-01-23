list=['parvinder','singh',1,5.3]
print(list)
print('----------------------------------------------------------------------------')
print(list[0], '= 1st element of the list')
print('----------------------------------------------------------------------------')
print(list[1], '= 2nd element of the list')
print('----------------------------------------------------------------------------')
print(list[2], '= 3rd element of the list')
print('----------------------------------------------------------------------------')
print(list[3], '= 4th element of the list')
print('----------------------------------------------------------------------------')
print(list[-1], '= last element of the list')
print('----------------------------------------------------------------------------')
print(list[-2], '= second last element of the list')
print('----------------------------------------------------------------------------')
print(list[-3], '= thirdn last element of the list')
print('----------------------------------------------------------------------------')
print(list[-4], '= 4th last element of the list')
print('----------------------------------------------------------------------------')
list[1]='anttal'
print('changing the second element',list)
print('----------------------------------------------------------------------------')
print('printing the whole list using for loop')
for i in list:
	print(i)
print('----------------------------------------------------------------------------')
if 'parvinder' in list:
	print("checking whether the element 'parvinder' is present in the list")
print('----------------------------------------------------------------------------')
print('checking the length of the list:-')
print(len(list))
print('----------------------------------------------------------------------------')
list.append(1996)
print('adding one element to the list')
print(list)
print('----------------------------------------------------------------------------')
list.remove(1996)
print('Removing the element in the list')
print(list)
print('----------------------------------------------------------------------------')
list.pop()
print('popping the last element of the list')
print(list)
print('----------------------------------------------------------------------------')
del list[1]
print('deleting the 2nd element of the list')
print(list)
print('----------------------------------------------------------------------------')
x=list.copy()
print('Copying the elements of the list')
print(x)
print('----------------------------------------------------------------------------')
list1=['singh',2]
list.extend(list1)
print('extending the list')
print(list)
print('----------------------------------------------------------------------------')
list.insert(4,20)
print('inserting the element into a specific position')
print(list)
print('----------------------------------------------------------------------------')
list.reverse()
print('reverse the list')
print(list)
print('----------------------------------------------------------------------------')
list2=[30,5,35,60,53,27]
list3=['W','A','S','D']
print('sorting the list')
list2.sort()
list3.sort()
print(list2)
print(list3)
print('----------------------------------------------------------------------------')
list.clear()
print('clear the list')
print(list)
print('----------------------------------------------------------------------------')




















