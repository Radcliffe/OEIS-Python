# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A045763

from sympy import divisor_count, totient
def A045763(n): return n+1-divisor_count(n)-totient(n) # _Chai Wah Wu_, Sep 02 2024

