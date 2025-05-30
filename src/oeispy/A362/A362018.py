# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A362018

from itertools import count, islice
def A362018_gen(startvalue=0): # generator of terms >= startvalue
    for k in count(max(startvalue,0)):
        c = iter(str(1<<k))
        if any(map(lambda b:all(map(lambda a:a!=b,c)),str(k**2))):
            yield k
A362018_list = list(islice(A362018_gen(),100))

