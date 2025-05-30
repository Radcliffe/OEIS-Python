# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A354972

from itertools import count, islice
from sympy import prime, isprime
def A354972_gen(): # generator of terms
    for n in count(1):
        if isprime(sum(prime(i+n) % prime(i) for i in range(1,n+1))):
            yield n
A354972_list = list(islice(A354972_gen(),10)) # _Chai Wah Wu_, Jun 20 2022

