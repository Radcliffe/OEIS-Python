# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A045715

from itertools import chain, count, islice
def A045715_gen(): # generator of terms
    return chain.from_iterable(primerange(9*(m:=10**l),10*m) for l in count(0))
A045715_list = list(islice(A045715_gen(),40)) # _Chai Wah Wu_, Dec 08 2024

