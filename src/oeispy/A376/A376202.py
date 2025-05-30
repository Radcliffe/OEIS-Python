# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376202

from math import gcd
def A376202(n):
    c = 0
    for x in range(1,n):
        if gcd(x,n) == 1:
            for y in range(x,n):
                if gcd(y,n)==gcd(z:=x+y,n)==1 and not (w:=z**2-x*y)//gcd(w,x*y*z)%n:
                    c += 1
    return c # _Chai Wah Wu_, Oct 06 2024

