# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356177

from itertools import count, islice, product
def simb(n): s = str(n); return all(s.count(d)%2==int(d)%2 for d in set(s))
def pals(): # generator of palindromes
    digits = "0123456789"
    for d in count(1):
        for p in product(digits, repeat=d//2):
            if d > 1 and p[0] == "0": continue
            left = "".join(p); right = left[::-1]
            for mid in [[""], digits][d%2]:
                yield int(left + mid + right)
def agen(): yield from filter(simb, pals())
print(list(islice(agen(), 55))) # _Michael S. Branicky_, Jul 28 2022

