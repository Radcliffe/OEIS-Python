# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A212180

from sympy import factorint, divisors, prod
def P(n): return sorted(factorint(n).values())
def a046523(n):
    x=1
    while True:
        if P(n)==P(x): return x
        else: x+=1
def a057521(n): return 1 if n==1 else prod(p**e for p, e in factorint(n).items() if e != 1)
def a212173(n): return a046523(a057521(n))
def a(n):
    l=[]
    for d in divisors(n):
        x=a212173(d)
        if not x in l:l+=[x, ]
    return len(l)
print([a(n) for n in range(1, 51)]) # _Indranil Ghosh_, Jul 19 2017

