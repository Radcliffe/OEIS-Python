# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A186774

def A186774(n):
    if sum(int(d) for d in str(n)) == 1:
        return 0
    sn, k = str(n+1), 1
    while sn not in str(k):
        k *= n
    return k # _Chai Wah Wu_, Feb 13 2017

