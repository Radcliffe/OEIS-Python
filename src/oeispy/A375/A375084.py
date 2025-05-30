# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A375084

from math import comb
from itertools import islice, count
def A375084_gen(): # generator of terms
    c = 0
    for n in count(1):
        if (d:=next(a for a, b in (divmod(comb(j,k),n) for j in range(n+1) for k in range(j+1)) if not b))>c:
            c = d
            yield n
A375084_list = list(islice(A375084_gen(),10)) # _Chai Wah Wu_, Jul 30 2024

