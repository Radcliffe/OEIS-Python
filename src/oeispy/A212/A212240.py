# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A212240

from sympy import divisor_count
def A212240(n): return  n**4-sum((sum(divisor_count(i+1)*divisor_count(j-i) for i in range(j>>1))<<1)+(divisor_count(j+1>>1)**2 if j&1 else 0) for j in range(1,n-1)) # _Chai Wah Wu_, Jul 26 2024

