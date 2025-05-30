# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A359065

import sys
import math
from sympy.ntheory import primefactors
from sympy.ntheory import primerange
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return len(lst3)
n_primes=1000000
factors=[primefactors(n) for n in range(0,n_primes)]
primes=list(primerange(0, n_primes))
sequence=[4]
sums=[sequence[0]]
prime_factors=[f for f in factors[sequence[0]]]
big_n=8
while len(sequence)<big_n:
    new_a=False
    a=sequence[-1]+1
    while intersection(factors[a],prime_factors)!=0:
        a+=1
    n=len(sequence)
    while not new_a:
        new_sum=[a+sum for sum in sums]
        prime_sum=False
        for sum in new_sum:
            if sum in primes:
                prime_sum=True
        if not prime_sum and a not in primes:
            sequence.append(a)
            print(a,end=",")
            sys.stdout.flush()
            sums=sums+new_sum+[a]
            sums = list(dict.fromkeys(sums))
            prime_factors=prime_factors+factors[a]
            new_a=True
        else:
            a+=1
            while a in primes or intersection(factors[a],prime_factors)!=0:
                a+=1
print()

