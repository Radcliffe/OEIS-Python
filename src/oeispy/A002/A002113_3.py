# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A002113

from itertools import chain, count
A002113 = chain(k for k in count(0) if str(k) == str(k)[::-1])
print([next(A002113) for k in range(60)]) # _Jan P. Hartkopf_, Apr 10 2021

