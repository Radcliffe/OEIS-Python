# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A305498

from itertools import islice
def A305498_gen(): # generator of terms
    a = 2
    while True:
        yield (a<<1)-2
        a += a>>1
A305498_list = list(islice(A305498_gen(),70)) # _Chai Wah Wu_, Sep 20 2022

