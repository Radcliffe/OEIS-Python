# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A338228

from sympy import divisor_count, integer_nthroot
from sympy.ntheory.factor_ import core
def A338228(n):
    return n-divisor_count(integer_nthroot(n//core(n,2),2)[0]) # _Chai Wah Wu_, Feb 01 2021

