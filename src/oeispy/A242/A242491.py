# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A242491

from itertools import count, islice
from sympy.ntheory.factor_ import digits
def A242491_gen(): # generator of terms
    return (int(''.join(str(d) if d<4 else str(d+1) for d in digits(n,8)[1:])) for n in count(1))
A242491_list = list(islice(A242491_gen(),40)) # _Chai Wah Wu_, Mar 05 2024

