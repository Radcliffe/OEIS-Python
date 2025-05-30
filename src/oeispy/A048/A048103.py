# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A048103

from itertools import count, islice
from sympy import factorint
def A048103_gen(startvalue=1): # generator of terms >= startvalue
    return filter(lambda n:all(map(lambda d:d[1]<d[0],factorint(n).items())),count(max(startvalue,1)))
A048103_list = list(islice(A048103_gen(),30)) # _Chai Wah Wu_, Jan 05 2023

