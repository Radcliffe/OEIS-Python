# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A058899

from itertools import count, islice, combinations_with_replacement
from sympy.ntheory import digits
def A058899_gen(startvalue=1): # generator of terms >= startvalue
    for n in count(max(startvalue,1)):
        for l in count(1):
            if 2*l*n < 3**(l-1):
                yield n
                break
            for d in combinations_with_replacement((0,1,2),l):
                if (s:=sum(d)) > 0 and sorted(digits(s*n,3)[1:]) == list(d):
                    break
            else:
                continue
            break
A058899_list = list(islice(A058899_gen(),20)) # _Chai Wah Wu_, May 10 2023

