# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A297574

def A297574(n):
    m = n+1
    mn = m*n
    while pow(2,m,mn) != pow(2,n,mn):
        m += 1
        mn += n
    return m # _Chai Wah Wu_, Jan 04 2018

