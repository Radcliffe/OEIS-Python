# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A318322

from functools import reduce
from sympy import factorint
def A318322(n): return sum(sum(reduce(lambda x,y:(x[0],sum(x)) if int(y) else (sum(x),x[1]),bin((e<<1)-1)[-1:2:-1],(1,0))) for e in factorint(n).values()) # _Chai Wah Wu_, May 18 2023

