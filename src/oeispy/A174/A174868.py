# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A174868

from itertools import accumulate, count, islice
from functools import reduce
def A174868_gen(): # generator of terms
    return accumulate((sum(reduce(lambda x,y:(x[0],x[0]+x[1]) if int(y) else (x[0]+x[1],x[1]),bin(n)[-1:2:-1],(1,0))) for n in count(1)),initial=0)
A174868_list = list(islice(A174868_gen(),30)) # _Chai Wah Wu_, May 07 2023

