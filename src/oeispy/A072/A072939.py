# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A072939

from itertools import count, islice
def A072939_gen(startvalue=2): return filter(lambda n:(~(n-1)&(n-2)).bit_length()&1,count(max(startvalue,2))) # generator of terms >= startvalue
A072939_list = list(islice(A072939_gen(),30)) # _Chai Wah Wu_, Jul 05 2022

