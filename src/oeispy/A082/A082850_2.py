# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A082850

from itertools import count, islice
def A082850_gen(): # generator of terms
    S = []
    for n in count(1):
        yield from (m:=S+[n])
        S += m #
A082850_list = list(islice(A082850_gen(),20)) # _Chai Wah Wu_, Mar 06 2023

