# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A337140

from itertools import count, islice
from sympy import primefactors
def A337140_gen(startvalue=2): # generator of terms >= startvalue
    return filter(lambda n: n&1^1 or not all(p&2 for p in primefactors(n>>(~n & n-1).bit_length())), count(max(startvalue,2)))
A337140_list = list(islice(A337140_gen(),30)) # _Chai Wah Wu_, Aug 21 2024

