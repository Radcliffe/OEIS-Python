# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A020451

from sympy import primerange
def checkd(a, c):
    b =  set(int(i) for i in set(str(a)))
    return b.issubset(c)
for n in primerange(2, 2000000):
    if checkd(n, [1, 3]):
        print(n)
# _Abhiram R Devesh_, May 04 2015

