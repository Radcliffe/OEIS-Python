# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A372075

from itertools import islice
def A372075_gen(): # generator of terms
    yield (a:=1)
    while True: yield (a:=a+10**len(s:=str(a))*sum(map(int,s)))
A372075_list = list(islice(A372075_gen(),20)) # _Chai Wah Wu_, Jun 16 2024

