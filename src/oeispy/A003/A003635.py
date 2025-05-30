# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A003635

from itertools import count, islice, combinations_with_replacement
def A003635_gen(startvalue=1): # generator of terms >= startvalue
    for n in count(max(startvalue,1)):
        for l in count(1):
            if 9*l*n < 10**(l-1):
                yield n
                break
            for d in combinations_with_replacement(range(10),l):
                if (s:=sum(d))>0 and sorted(str(s*n)) == [str(e) for e in d]:
                    break
            else:
                continue
            break
A003635_list = list(islice(A003635_gen(),20)) # _Chai Wah Wu_, May 09 2023

