# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A054429

from itertools import count, islice
def A054429_gen(): # generator of terms
    return (m for n in count(0) for m in range((1<<n+1)-1,(1<<n)-1,-1))
A054429_list = list(islice(A054429_gen(),30)) # _Chai Wah Wu_, Jul 27 2023

