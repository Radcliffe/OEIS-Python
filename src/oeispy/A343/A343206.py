# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A343206

from sympy.functions.combinatorial.numbers import stirling, bernoulli
def A343206(n): return sum(stirling(n,i,signed=True)*bernoulli(i) for i in range(n+1)).p # _Chai Wah Wu_, Apr 08 2021

