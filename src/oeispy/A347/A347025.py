# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A347025

from itertools import combinations
def anysetunion(family):
    for s in family:
        allrest = 0
        for r in family:
            if r != s and r&s == r:
                allrest |= r
                if allrest == s:
                    return True
    return False
def a(n):
    if n < 2: return n
    m = 2
    while True:
        allfailed = True
        for family in combinations(range(1, 2**n), m):
            unionfound = anysetunion(family)
            allfailed &= unionfound
            if not unionfound: break
        if allfailed: return m - 1
        m += 1
print([a(n) for n in range(5)]) # _Michael S. Branicky_, Nov 09 2021

