# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A061418

from itertools import islice
def A061418_gen(): # generator of terms
    a = 2
    while True:
        yield a
        a += a>>1
A061418_list = list(islice(A061418_gen(),70)) # _Chai Wah Wu_, Sep 20 2022

