# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A097315

from itertools import islice
def A097315_gen(): # generator of terms
    x, y = 30, 10
    while True:
        yield y//10
        x, y = x*19+y*60, x*6+y*19
A097315_list = list(islice(A097315_gen(),20)) # _Chai Wah Wu_, Apr 24 2025

