# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342567

from primesieve.numpy import n_primes
primesarray = numpy.array(n_primes(10005,1))
for i in range (2, 10003):
     print(((primesarray[i]**2)-(primesarray[i-1]*primesarray[i+1]))//2)
     # _Karl-Heinz Hofmann_, Jun 20 2021

