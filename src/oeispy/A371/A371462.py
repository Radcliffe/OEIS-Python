# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A371462

from itertools import count, islice
def A371462_gen(startvalue=0): # generator of terms >= startvalue
    return filter(lambda n:sum(map(int,(s:=str(n))))**2<<1 == len(s)*sum(int(d)**2 for d in s), count(max(startvalue,0)))
A371462_list = list(islice(A371462_gen(),20)) # _Chai Wah Wu_, Mar 28 2024

