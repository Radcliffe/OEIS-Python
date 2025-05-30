# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A308605

from sympy import divisors
def a308605(n):
    s = set([0])
    for d in divisors(n):
        s = s.union(set(x + d for x in s))
    return len(s) # _David Radcliffe_, Dec 22 2022

