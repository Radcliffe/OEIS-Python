# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A362090

from gmpy2 import digits
def A362090(n): return sum((-(1<<i) if int(j)&1 else 1<<i) for i, j in enumerate(digits(n,3).replace('1','01').replace('2','02')[::-1]) if j!='0') # _Chai Wah Wu_, Apr 12 2023

