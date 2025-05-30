# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A067874

from itertools import count, islice
from sympy import factorint
def A067874_gen(startvalue=2): # generator of terms >= startvalue
    return filter(lambda k:max(factorint(k-1).values(),default=1)==1 and max(factorint(k+1).values())==1, count(max(startvalue+(startvalue&1),2),2))
A067874_list = list(islice(A067874_gen(),20)) # _Chai Wah Wu_, Apr 24 2024

