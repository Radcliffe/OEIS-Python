# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A069942

from sympy import divisors
A069942 = [n for n in range(1,10**5) if sum(list(map(lambda x: int(str(x)[::-1]) if x < n else 0, divisors(n)))) == int(str(n)[::-1])] # _Chai Wah Wu_, Aug 13 2014

