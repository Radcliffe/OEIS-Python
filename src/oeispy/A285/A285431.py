# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A285431

from itertools import islice
def A285431_gen(): # generator of terms
    a, l = [1,1], 0
    while True:
        yield from a[l:]
        c = sum(([1,1,0] if d else [1,1] for d in a),start=[])
        l, a = len(a), c
A285431_list = list(islice(A285431_gen(),30)) # _Chai Wah Wu_, Nov 30 2023

