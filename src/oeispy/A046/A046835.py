# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A046835

from itertools import count, islice
def A046835_gen(startvalue=1): # generator of terms >= startvalue
    for k in count(max(startvalue,1)):
        if k%10:
            c = iter(str(k**2)[1:-1])
            if all(map(lambda b:any(map(lambda a:a==b,c)),str(k))):
                yield k
A046835_list = list(islice(A046835_gen(),20)) # _Chai Wah Wu_, Apr 03 2023

