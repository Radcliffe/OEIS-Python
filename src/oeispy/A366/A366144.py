# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A366144

from sympy import divisor_count
def A366144(n): return n*d if (q:=divmod(n,d:=int(divisor_count(n))))[1] else q[0] # _Chai Wah Wu_, Oct 02 2023

