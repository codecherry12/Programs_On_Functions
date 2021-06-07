#filter function
def fun1(a):
    return a%2==0
l=[2,5,6,23,34,68,12]
f1=filter(fun1,l)
print(f1,type(f1))
print(list(f1))#we can make use of filter only once
l1=list(f1)
print(l1)#we will get null

#lambda function
v4=lambda x:x%2==0
f2=filter(f4,l)
for i in f2:
    print(i)

def fun1(a):
    return a**3
print()
print(fun1(3))
print(fun1(5))
v2=lambda x,y:x+y
print()
print(v2(2,7))

v3=lambda x,y:x if x>y else y
print()
print(v3(4,8))
print(v3(6,3))

#map function
l=[1,2,3,4,5,6,7]
def fun2(a):
    return a*a

m1=map(fun2,l)
print(list(m1),type(m1))

v=lambda x:x*x
m2=map(v5,l)
print(m2,list(m2),type(m1))
#reduce function
#reduces the sequence of elements into a single value
#reduce will be imported from functools
from functools import *
l=[1,2,3,4,5,6,7]
def fun3(a,b):
    return a+b
r3= reduce(fun3,l)
print(r3)

v6=lambda x,y:x+y
r4=reduce(v6,l)
print(r4)
