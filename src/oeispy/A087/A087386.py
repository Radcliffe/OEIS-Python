# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A087386

from itertools import count
from sympy import isprime
def A087386(n):
    q =(c:=n+1-x)*x+int(str(c)[-2::-1] or 0) if n+1<(x:=10**(len(str(n+1>>1))-1))+(y:=10*x) else (c:=n+1-y)*y+int(str(c)[::-1] or 0)
    return next(p for p in count(q+1,q) if isprime(p)) # _Chai Wah Wu_, Jul 11 2024

