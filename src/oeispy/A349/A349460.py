# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349460

from itertools import islice, count
def A349460(): return filter(lambda n: set(str(n)) <= {'0','2','4'},(n*n for n in count(0)))
A349460_list = list(islice(A349460(),20)) # _Chai Wah Wu_, Nov 19 2021

