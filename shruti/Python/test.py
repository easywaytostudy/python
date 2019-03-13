###question 1
for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        print(i,end=",")
print()

question 2
def fact(x):
    if x==0 or x==1:
        return 1
    result = x*fact(x-1)
    return result

y = int(input())
z = fact(y)
print(z)


dict = {}
n = int(input())
for i in range (1,n):
    dict[i] = i*i
