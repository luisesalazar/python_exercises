def reduce(n):
    if not n:
        return 0

    return n[0] + reduce(n[1:])


n= [1,2,3,4,5]
print(reduce(n))