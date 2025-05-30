# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A328803

from itertools import count, islice
from sympy.solvers.diophantine.diophantine import diop_DN
from sympy import factorint
def A328803_gen(): # generator of terms
    return map(lambda n: min((a+b for a, b in diop_DN(-1,n))), filter(lambda n:(lambda m:all(d&3!=3 or m[d]&1==0 for d in m))(factorint(n)), count(0)))
A328803_list = list(islice(A328803_gen(),30)) # _Chai Wah Wu_, Sep 09 2022

