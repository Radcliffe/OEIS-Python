# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A004722

def A004722(n):
    l = len(str(n))
    m = (10**l-1)//3
    k = n + l - int(n+l < m)
    return 2 if k == m else int(str(k).replace('3','')) # _Chai Wah Wu_, Apr 20 2021

