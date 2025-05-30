# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A189715

from sympy import integer_log
def A189715(n):
    def f(x): return n+x-sum(((m:=x//9**i)-1)//9+(m-4)//9+(m-6)//9+(m-7)//9+4 for i in range(integer_log(x,9)[0]+1))
    m, k = n, f(n)
    while m != k: m, k = k, f(k)
    return m # _Chai Wah Wu_, Feb 15 2025

