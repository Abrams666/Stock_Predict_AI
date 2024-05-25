def arrangement(a,b):
    total=a**b
    c=[list() for _ in range(total)]
    for i in range(total):
        d=i
        for j in range(b):
            c[i].append(d%a)
            d=d//a
    return c