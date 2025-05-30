# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A161601

from itertools import count, islice
def A161601_gen(startvalue=1): # generator of terms >= startvalue
    return filter(lambda n:n<int(bin(n)[-1:1:-1],2),count(max(startvalue|1,1),2))
A161601_list = list(islice(A161601_gen(),20)) # _Chai Wah Wu_, Jan 19 2023

