# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A380121

from math import comb as C
def a(n): return C(n,(n+3)//4-1)*C(n,(n+1)//4)+C(n,(3*n+1)//4)*C(n,(3*n+3)//4) if n>0 else 1; print([a(n) for n in range(31)])

