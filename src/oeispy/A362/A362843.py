# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A362843

from itertools import count, islice
def A362843_gen(startvalue=0): # generator of terms >= startvalue
    return filter(lambda n:n==sum(int(d)**((i<<1)+1) for i,d in enumerate(str(n))),count(max(startvalue,0)))
A362843_list = list(islice(A362843_gen(),12)) # _Chai Wah Wu_, Jun 26 2023

