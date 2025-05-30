# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349809

from itertools import count
from sympy import factorint
def A349809(n):
    for i in count(n**2-(n%2)-1,-2):
        fs = factorint(i)
        if len(fs) == 2 == sum(fs.values()):
            return n**2-i # _Chai Wah Wu_, Dec 06 2021

