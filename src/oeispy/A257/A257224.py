# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A257224

from itertools import count, islice
from sympy import divisors
def A257224_gen(): return filter(lambda n:any('7' in str(d) for d in divisors(n, generator=True)), count(1))
A257224_list = list(islice(A257224_gen(), 20)) # Chai Wah Wu, Dec 27 2021

