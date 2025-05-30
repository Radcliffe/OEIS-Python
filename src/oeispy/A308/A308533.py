# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A308533

from itertools import islice, count
from sympy.ntheory.factor_ import antidivisors
def A308533gen(): # generator of terms
    for n in count(3):
        a = antidivisors(n)
        if int(''.join(str(s) for s in a)) % sum(a) == 0:
            yield n
A308533_list = list(islice(A308533gen(),22)) # _Chai Wah Wu_, Dec 08 2021

