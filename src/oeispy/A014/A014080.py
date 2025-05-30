# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A014080

from itertools import count, islice
def A014080_gen(): # generator of terms
    return (n for n in count(1) if sum((1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)[int(d)] for d in str(n)) == n)
A014080_list = list(islice(A014080_gen(),4)) # _Chai Wah Wu_, Feb 18 2022

