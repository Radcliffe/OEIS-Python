# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A032531

from math import comb, isqrt
from collections import Counter
def idx(n): return n - comb((1+isqrt(8+8*n))//2, 2)
def aupton(nn):
    num, alst, inventory = 0, [0], Counter([0])
    for n in range(1, nn+1):
        c = inventory[idx(n)]
        alst.append(c)
        inventory[c] += 1
    return alst
print(aupton(93)) # _Michael S. Branicky_, May 07 2023

