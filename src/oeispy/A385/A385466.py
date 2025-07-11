# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A385466

from sympy import primerange
primes = list(primerange(2, 2000))
diffs = [primes[i+1] - primes[i] for i in range(len(primes)-1)]
local_max_asals = []
for i in range(1, len(diffs)-1):
    if diffs[i] > diffs[i-1] and diffs[i] > diffs[i+1]:
        local_max_asals.append(primes[i+1])
print(local_max_asals[:70])

