# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A180301

from num2words import num2words
def n2w(n):
    return num2words(n).replace(" and", "").replace(chr(44), "")
def afind(limit, start=1):
    last, t = start, start+1
    print(start, end=", ")
    while t <= limit:
        target = n2w(last)
        while n2w(t) <= target:
            t += 1
            if t > limit: return
        last = t
        print(t, end=", ")
afind(3000) # _Michael S. Branicky_, Sep 16 2021

