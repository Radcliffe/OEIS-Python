# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350579

from itertools import count
from collections import Counter
def A350579(n):
    b, bcounter = 0, Counter({0})
    for m in count(1):
        if bcounter[b] == n: return b
        b += -m if b-m >= 0 and bcounter[b-m] <= bcounter[b+m] else m
        bcounter[b] += 1 # _Chai Wah Wu_, Jan 08 2022

