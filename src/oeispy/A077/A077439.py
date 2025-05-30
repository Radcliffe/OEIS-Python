# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A077439

from itertools import count, islice
def A077429_gen(): # generator of terms
    for m in count(0):
        s = bin(m)[2:]
        if len(s)&1: s='0'+s
        n = int(''.join({'00':'0','01':'1','10':'4','11':'9'}[s[i:i+2]] for i in range(0,len(s),2)))
        if set(str(n**2)) <= {'0','1','4','9'}:
            yield n
A077429_list = list(islice(A077429_gen(),20)) # _Chai Wah Wu_, Dec 19 2023

