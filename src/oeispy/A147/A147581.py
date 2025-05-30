# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A147581

from sympy import integer_log
def A147581(n):
    def bisection(f,kmin=0,kmax=1):
        while f(kmax) > kmax: kmax <<= 1
        while kmax-kmin > 1:
            kmid = kmax+kmin>>1
            if f(kmid) <= kmid:
                kmax = kmid
            else:
                kmin = kmid
        return kmax
    def f(x):
        c = n+x
        for i23 in range(integer_log(x,23)[0]+1):
            for i19 in range(integer_log(x23:=x//23**i23,19)[0]+1):
                for i17 in range(integer_log(x19:=x23//19**i19,17)[0]+1):
                    for i13 in range(integer_log(x17:=x19//17**i17,13)[0]+1):
                        for i11 in range(integer_log(x13:=x17//13**i13,11)[0]+1):
                            for i7 in range(integer_log(x11:=x13//11**i11,7)[0]+1):
                                for i5 in range(integer_log(x7:=x11//7**i7,5)[0]+1):
                                    c -= integer_log(x7//5**i5,3)[0]+1
        return c
    return 111546435*bisection(f,n,n) # _Chai Wah Wu_, Oct 22 2024

