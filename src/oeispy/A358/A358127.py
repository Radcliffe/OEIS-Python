# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A358127

from sympy import nextprime
from math import gcd
from itertools import combinations
pr, terms = [2,3], []
for i in range(100):
    terms.append(len(set([gcd(t[0]+1, t[1]+1) for t in combinations(pr,2)])))
    pr.append(nextprime(pr[-1]))
print(terms)

