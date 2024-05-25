def array_plus(a):
    b=0
    for i in range(len(a)):
        b=b+a[i]
    return b

a=[1,2,3]

print(array_plus(a))