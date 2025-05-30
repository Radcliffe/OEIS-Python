# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A085908

from itertools import count
from sympy import integer_log
def A085908(n):
    if n<2: return n
    def f(x):
        c = 0
        for i in range(integer_log(x,7)[0]+1):
            for j in range(integer_log(m:=x//7**i,5)[0]+1):
                for k in range(integer_log(r:=m//5**j,3)[0]+1):
                    c += (r//3**k).bit_length()
        return c
    for l in count(0):
        kmin, kmax = n*10**l-1, (n+1)*10**l-1
        mmin, mmax = f(kmin), f(kmax)
        if mmax>mmin:
            while kmax-kmin > 1:
                kmid = kmax+kmin>>1
                mmid = f(kmid)
                if mmid > mmin:
                    kmax, mmax = kmid, mmid
                else:
                    kmin, mmin = kmid, mmid
            return kmax # _Chai Wah Wu_, Sep 17 2024

