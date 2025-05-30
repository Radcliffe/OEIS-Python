# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A375019

"""
Note that this code generates all terms <= n, not the nth term.
This code can be further optimized with an O(n log n) sieve, which we do not write here.
"""
n = 10**5  # replace this number with whatever limit
from sympy import primefactors, prod
def rad(n): return 1 if n < 2 else prod(primefactors(n))
# Function to help determine whether a value is a term.
def is_term(k: int):
    # Calculate rad((k^2-1)*k^2) = rad((k-1)*k*(k+1)).
    rad_abc = rad(k-1) * rad(k) * rad(k+1)
    if k % 2 == 1:
        rad_abc //= 2  # 2 is double-counted as a prime factor. No other multiple-counts are possible.
    return rad_abc < k**2
# The final sequence.
a = list(filter(is_term, range(2, n+1))) # _William Hu_, Aug 09 2024

