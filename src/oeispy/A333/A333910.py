# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A333910

from itertools import count, islice
from collections import Counter
from sympy import factorint
def A333910_gen(): # generator of terms
    return filter(lambda n:all(p & 3 != 3 or e & 1 == 0 for p, e in sum((Counter(factorint(1+p))+Counter({p:e-1}) for p ,e in factorint(n).items()),start=Counter()).items()),count(1))
A333910_list = list(islice(A333910_gen(),30)) # _Chai Wah Wu_, Jun 27 2022

