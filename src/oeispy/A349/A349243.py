# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349243

from itertools import islice, count
def A349243(): return filter(lambda n: set(str(n*(n+1)//2)) <= {'1','3','5','7','9'}, count(0))
A349243_list = list(islice(A349243(),20)) # _Chai Wah Wu_, Nov 22 2021

