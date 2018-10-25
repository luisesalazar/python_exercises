#reduce was eliminated from python3
from functools import reduce

def double(x):
    return x*2

print(double(5))

#with lambda
d= lambda x: x*2

print(d(5))

#map aplies a function to each elements of a list
l=[1,2,3,4,5,6]
l2= map(double, l)

#map and lambda
l3= map(lambda x: x*2, l)

#filter and lambda
l4= filter(lambda x: x%2==0, l)

#reduce
l5= reduce(lambda x, y: x+y, l)

print(list(l2))
print(list(l3))
print(list(l4))
print(l5)