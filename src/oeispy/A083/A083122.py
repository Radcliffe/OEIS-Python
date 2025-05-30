# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A083122

from itertools import count, islice, product
def pals(digs):
    yield from digs
    for d in count(2):
        for p in product(digs, repeat=d//2):
            left = "".join(p)
            for mid in [[""], digs][d%2]:
                yield left + mid + left[::-1]
def folds(s): # generator of suffixes of palindromes starting with s
    for i in range((len(s)+1)//2, len(s)+1):
        for mid in [True, False]:
            t = s[:i] + (s[:i-1][::-1] if mid else s[:i][::-1])
            if t.startswith(s):
                yield t[len(s):]
    yield from ("".join(p)+s[::-1] for p in pals("12"))
def agen():
    s, seen = "1", {"1"}; yield 1
    while True:
        for t in folds(s):
            if len(t) > 0 and set(t) != {"1"} and t not in seen: break
        s = t; seen.add(t); yield int(t)
print(list(islice(agen(), 33))) # _Michael S. Branicky_, Aug 09 2022

