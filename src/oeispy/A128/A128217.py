# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A128217

from itertools import count, islice
from math import isqrt
def A128217_gen(startvalue=0): # generator of terms >= startvalue
    return filter(lambda n:(m:=n<<4)<(k:=(isqrt(n)<<2)+1)**2 or m>(k+2)**2, count(max(startvalue,0)))
A128217_list = list(islice(A128217_gen(),40)) # _Chai Wah Wu_, Jun 06 2025

