# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A361075

import numpy
from sympy import nextprime, sieve, primepi
k_upto = 14 * 10**6
array = numpy.zeros(k_upto,dtype="i4")
sieve_max_number = primepi(nextprime(k_upto // 255255))
for s in range(2,sieve_max_number):
    array[sieve[s]:k_upto][::sieve[s]] += 1
for s in range(2,sieve_max_number):
    array[sieve[s]**2:k_upto][::sieve[s]**2] = 0
print([k for k in range(1,k_upto,2) if array[k] == 7])

