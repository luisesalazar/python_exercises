#1,1,2,3,5,8,13,21,34,55,89 etc
cache= {}
def fibonacci(n):
    if n in cache:
        return cache[n]

    if n == 1:
        value= 1
    elif n == 2:
        value= 1
    elif n > 2:
        value= fibonacci(n-1) + fibonacci(n-2)

    cache[n]= value
    return value


for i in range(1, 100):
    print(i, ": ", fibonacci(i))

print(cache)