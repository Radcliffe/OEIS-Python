# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A307907

from sympy import integer_log, primefactors
def A307907(n): return integer_log(n,max(primefactors(n)))[0] # _Chai Wah Wu_, Oct 12 2024

