# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A340040

from itertools import count, takewhile
def aupto(lim):
    sqs = list(takewhile(lambda x: x <= lim, (i**2 for i in count(1))))
    cbs = list(takewhile(lambda x: x <= lim, (i**3 for i in count(1))))
    sms = set(s + t for s in sqs for t in cbs if 0 < s < t and s + t < lim)
    return sorted(sms)
print(aupto(540)) # _Michael S. Branicky_, Sep 12 2021

