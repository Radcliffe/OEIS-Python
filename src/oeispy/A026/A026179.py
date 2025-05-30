# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A026179

from sympy import integer_log
def A026179(n):
    def f(x): return n-1+x-sum(((x//3**i)-2)//3+1 for i in range(integer_log(x,3)[0]+1))
    m, k = n, f(n)
    while m != k: m, k = k, f(k)
    return m # _Chai Wah Wu_, Feb 15 2025

