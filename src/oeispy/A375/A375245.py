# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A375245

from sympy import mobius, integer_nthroot
def A375245(n): return int(sum(mobius(k)*(n//k**4) for k in range(1, integer_nthroot(n,4)[0]+1)))

