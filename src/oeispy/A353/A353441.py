# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A353441

from itertools import count, islice
from sympy import multiplicity, n_order
def A353441_gen(startvalue=1): # generator of terms >= startvalue
    for a in count(max(startvalue,1)):
        m2, m5 = (~a&a-1).bit_length(), multiplicity(5,a)
        k, m = 10**max(m2,m5), 10**n_order(10,a//(1<<m2)//5**m5)-1
        if '5' in str(c:=k//a) or '5' in str(m*k//a-c*m):
            yield a
A353441_list = list(islice(A353441_gen(),20)) # _Chai Wah Wu_, May 01 2023

