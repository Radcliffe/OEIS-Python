# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A007955

from math import isqrt
from sympy import divisor_count
def A007955(n):
    d = divisor_count(n)
    return isqrt(n)**d if d % 2 else n**(d//2) # _Chai Wah Wu_, Jan 05 2022

