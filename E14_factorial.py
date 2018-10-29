def factorial_num(n):
    if n==0:
        return 1

    return n * factorial_num(n-1)

def factorial(n):
    if not n:
        return 1

    return n[0] * factorial(n[1:])


n= int(input("Factorial de: "))
n= list(range(1, n+1))
n.reverse()
#r= factorial_num(n)
r= factorial(n)
print(r)