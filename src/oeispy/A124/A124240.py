# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A124240

from itertools import islice, count
from sympy.ntheory.factor_ import reduced_totient
def A124240gen(): return filter(lambda n:n % reduced_totient(n) == 0,count(1))
A124240_list = list(islice(A124240gen(),20)) # _Chai Wah Wu_, Dec 11 2021

