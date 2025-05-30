# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A277776

from itertools import chain, count, islice
from sympy.ntheory import sqrt_mod_iter
def A277776_gen(): # generator of terms
    return chain.from_iterable((sorted(filter(lambda m:1<m<n-1,sqrt_mod_iter(1,n))) for n in count(2)))
A277776_list = list(islice(A277776_gen(),30)) # _Chai Wah Wu_, Oct 26 2022

