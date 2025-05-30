# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A354301

from itertools import count, islice
def wt(n): return bin(n).count("1")
def agen(): # generator of terms
    n, fn, fn1, fn2, wtn, wtn1, wtn2 = 0, 1, 1, 2, 1, 1, 1
    for n in count(0):
        if wtn == wtn1 == wtn2: yield n
        fn, fn1, fn2 = fn1, fn2, fn2*(n+3)
        wtn, wtn1, wtn2 = wtn1, wtn2, wt(fn2)
print(list(islice(agen(), 4))) # _Michael S. Branicky_, May 23 2022

