def febo(n):
    a ,b = 0,1
    for i in range(n):
        print(a)
        a, b = b , a+b


def feboRecur(n):
    for i in range(n):
        print(feboRecurssive(i))

def feboRecurssive(n):
    if n <=1:
        return n
    else:
        return feboRecurssive(n-1) + feboRecurssive(n-2)


n = 10 

feboRecur(n)
febo(n)