# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A372046

from itertools import count, islice
from sympy import factorint
def A372046_gen(startvalue=4): # generator of terms >= startvalue
    for n in count(max(startvalue,4)):
        f = factorint(n)
        if sum(f.values()) > 1:
            c = 0
            for p in sorted(f):
                a = pow(10,len(s:=str(p)),n)
                q = int(s[::-1])
                for _ in range(f[p]):
                    c = (c*a+q)%n
            if not c:
                yield n
A372046_list = list(islice(A372046_gen(),5)) # _Chai Wah Wu_, Apr 24 2024

