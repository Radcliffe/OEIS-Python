# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A065363

def a(n):
    s=0
    x=0
    while n>0:
        x=n%3
        n=n//3
        if x==2:
            x=-1
            n+=1
        s+=x
    return s
print([a(n) for n in range(101)]) # _Indranil Ghosh_, Jun 06 2017

