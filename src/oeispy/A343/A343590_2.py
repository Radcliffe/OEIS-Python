# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A343590

from sympy import isprime
def f(w,dir):
    if dir == 1:
        for s in w:
            for t in range(int(s[-1])+1,10,2):
                yield s+str(t)
    else:
        for s in w:
            for t in range(1-int(s[-1])%2,int(s[-1]),2):
                yield s+str(t)
A343590_list = []
for l in range(5):
    for d in '123456789':
        x = d
        for i in range(1,l+1):
            x = f(x,(-1)**i)
        A343590_list.extend([int(p) for p in x if isprime(int(p))])
        if l > 0:
            y = d
            for i in range(1,l+1):
                y = f(y,(-1)**(i+1))
            A343590_list.extend([int(p) for p in y if isprime(int(p))]) # _Chai Wah Wu_, Apr 25 2021

