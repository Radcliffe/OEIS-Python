# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A062296

from sympy.ntheory import digits
def A062296(n):
    s = digits(n,3)[1:]
    return n+1-(3**s.count(2)<<s.count(1)) # _Chai Wah Wu_, Jul 24 2025

