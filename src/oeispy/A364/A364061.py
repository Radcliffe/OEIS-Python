# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A364061

from sympy import factorint
from itertools import count, islice
def A364061_gen(startvalue=2): # generator of terms >= startvalue
    return filter(lambda n:(l:=(~n&n-1).bit_length()) < min(factorint(m:=n>>l).values(),default=0) or m==1, count(max(startvalue+startvalue&1,2),2))
A364061_list = list(islice(A364061_gen(),30)) # _Chai Wah Wu_, Jul 14 2023

