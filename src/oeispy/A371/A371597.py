# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A371597

from sympy import divisors
def A371597(n): return sum(m for m in range(1, (n**2>>2)+1) if (d:=divisors(m))[((l:=len(d))-1)>>1]+d[l>>1]==n)

