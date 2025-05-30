# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A071925

from itertools import islice, count
from sympy.utilities.iterables import multiset_permutations
def A071925gen(): # generator of terms
    for n in count(1):
        yield from (int('1'+''.join(p)) for p in multiset_permutations('0'*n+'1'*(n-1)))
A071925_list = list(islice(A071925gen(),30)) # _Chai Wah Wu_, Dec 06 2021

