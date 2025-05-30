# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A155562

from itertools import count, islice
from sympy import factorint
def A155562_gen(): # generator of terms
    return filter(lambda n:all((p & 3 != 3 and p & 7 < 5) or e & 1 == 0 for p, e in factorint(n).items()),count(0))
A155562_list = list(islice(A155562_gen(),30)) # _Chai Wah Wu_, Jun 27 2022

