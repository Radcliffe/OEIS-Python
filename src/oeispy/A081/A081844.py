# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A081844

from sympy import totient, n_order, divisors
def A081844(n): return sum(totient(d)//n_order(2,d) for d in divisors((n+1<<1)-1,generator=True) if d>1) + 1 # _Chai Wah Wu_, Apr 09 2024

