# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A055046

from itertools import count, islice
def A055046_gen(startvalue=1): # generator of terms >= startvalue
    return filter(lambda n:not (m:=(~n&n-1).bit_length())&1 and (n>>m)&7==3,count(max(startvalue,1)))
A055046_list = list(islice(A055046_gen(),30)) # _Chai Wah Wu_, Jul 09 2022

