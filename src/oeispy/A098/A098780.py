# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A098780

def A098780(n):
    s=""
    for i in range(n,0,-1):
        s+=bin(i)[2:]
    return int(s,2) # _Indranil Ghosh_, Jan 28 2017

