# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A070824

from sympy import divisor_count
def A070824(n): return 0 if n == 1 else divisor_count(n)-2 # _Chai Wah Wu_, Jun 03 2022

