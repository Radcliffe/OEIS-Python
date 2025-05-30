# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A357774

from itertools import count, islice
def A357774_gen(): # generator of terms
    for l in count(2):
        m = (10**(l+2)-1)//9
        for i in range(l,0,-1):
            k = m-10**i
            yield from (k-10**j for j in range(i-1,0,-1))
A357774_list = list(islice(A357774_gen(),30)) # _Chai Wah Wu_, Feb 19 2023

