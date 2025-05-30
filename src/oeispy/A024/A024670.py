# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A024670

from itertools import count, takewhile
def aupto(limit):
    cbs = list(takewhile(lambda x: x <= limit, (i**3 for i in count(1))))
    sms = set(c+d for i, c in enumerate(cbs) for d in cbs[i+1:])
    return sorted(s for s in sms if s <= limit)
print(aupto(1674)) # _Michael S. Branicky_, Sep 28 2021

