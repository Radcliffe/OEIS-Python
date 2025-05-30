# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A083866

from itertools import groupby, islice
def A083866_gen(startvalue=0): # generator of terms >= startvalue
    n, c = max(0,startvalue),0
    for k, g in groupby(bin(n)[2:]):
        c = c+len(list(g)) if k == '1' else (-c if len(list(g))&1 else c)
    while True:
        if c == 0: yield n
        n += 1
        c = c-t-1 if (t:=(~n & n-1).bit_length())&1 else t+1-c
A083866_list = list(islice(A083866_gen(),20)) # _Chai Wah Wu_, Mar 02 2023

