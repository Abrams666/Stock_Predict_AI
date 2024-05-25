def cross_multiplication(a,b):
    if (len(a)>=len(b)):
        len_ab=len(b)
    else:
        len_ab=len(a)
    c=[]
    for i in range(len_ab):
        d=a[i]*b[i]
        c.append(d)
    return c

a=[1,2,3]
b=[4,5,6]
c=cross_multiplication(a,b)

print(c)