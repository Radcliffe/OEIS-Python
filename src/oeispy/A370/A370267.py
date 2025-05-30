# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A370267

def A370267(n):
    def f(x): return n+x-sum(((y:=x>>(i<<1))-7>>3)+(y-1>>3)+2 for i in range((x.bit_length()>>1)+1))-sum(((z:=x>>(i<<1)+1)-5>>3)+(z-3>>3)+2 for i in range(x.bit_length()-1>>1))
    m, k = n, f(n)
    while m != k: m, k = k, f(k)
    return m # _Chai Wah Wu_, Mar 19 2025

