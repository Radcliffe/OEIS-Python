# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A367600

from itertools import count, islice
def A367338(n):
    nn = n + 10*(n%10)
    return next((nn+y for y in range(1, 10) if str(nn+y)[0] == str(y)), -1)
def agen():
    A367338_set = set()
    for n in count(1):
        A367338_set.add(A367338(n))
        if n not in A367338_set:
            yield n
        # A367338_set.discard(n-100) # uncomment if memory is an issue
print(list(islice(agen(), 86))) # _Michael S. Branicky_, Nov 28 2023

