# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349215

from math import prod
from sympy import factorint
def A349215(n):
    fs = factorint(n)
    return sum(a-1 for a in fs.keys())+prod(1+d for d in fs.values()) # _Chai Wah Wu_, Nov 11 2021

