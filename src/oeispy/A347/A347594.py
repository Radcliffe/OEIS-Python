# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A347594

from math import isqrt
A347594_list = [1]
for n in range(1,10**3):
    m = A347594_list[n-1]**2+n**2
    A347594_list.append((isqrt(m)+1)**2-m) # _Chai Wah Wu_, Sep 12 2021

