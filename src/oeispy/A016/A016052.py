# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A016052

from itertools import islice
def A016052_gen(): # generator of terms
    yield (a:=3)
    while True: yield (a:=a+sum(map(int,str(a))))
A016052_list = list(islice(A016052_gen(),20)) # _Chai Wah Wu_, Jun 16 2024

