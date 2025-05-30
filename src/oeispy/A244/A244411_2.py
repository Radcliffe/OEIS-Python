# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A244411

from sympy import divisor_count, sqrt
A244411_list = [1]
for n in range(1,10**5):
    d = divisor_count(n)
    if d > 2:
        q, r = divmod(d,2)
        s = str(n**q*(sqrt(n) if r else 1))
        if s == s[::-1]:
            A244411_list.append(n) # _Chai Wah Wu_, Aug 25 2015

