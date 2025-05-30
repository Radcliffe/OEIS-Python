# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A046834

from itertools import count, islice
def A046834_gen(startvalue=1): # generator of terms >= startvalue
    for k in count(max(startvalue,1)):
        c = iter(str(k**2)[1:-1])
        if all(map(lambda b:any(map(lambda a:a==b,c)),str(k))):
            yield k
A046834_list = list(islice(A046834_gen(),20)) # _Chai Wah Wu_, Apr 03 2023

