# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A352170

from sympy import sieve, isprime
for p in sieve.primerange(0, 10**6):
    if(all(isprime(q) for q in [p+4, 3*p+4, 3*p+8])):
        print (p, end=", ") # _Martin Ehrenstein_, Mar 09 2022

