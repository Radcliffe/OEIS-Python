# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A213239

[n for n in range(1,10**5) if sum([sum([int(x) for x in str(d)]) for d in range(2,n) if n % d and 2*n % d in [d-1,0,1]]) == sum([int(x) for x in str(n)])] # _Chai Wah Wu_, Aug 08 2014

