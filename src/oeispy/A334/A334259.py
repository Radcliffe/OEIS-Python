# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A334259

import sympy
from sympy import sieve
def digits_at(ss, n):
    ''' Extracts len(str(n)) digits at position n.'''
    t = len(str(n))
    s = ss[n:n+t]
    if s == '':
        return -1
    return int(s)
def self_locating(ss, n):
    return digits_at(ss,n) == n
SS = ""
for p in sieve.primerange(2, 100000):
    SS += str(p)
for i in range(100000):
    if self_locating(SS, i):
        print(i,end=",")

