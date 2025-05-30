# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A351928

from itertools import count
def A351928(n):
    kmax, m = 3**n, (3**(n-1)).bit_length()
    k2 = pow(2,m,kmax)
    for k in count(m):
        a = k2
        while a > 0:
            a, b = divmod(a,3)
            if b == 2:
                break
        else:
            return k
        k2 = 2*k2 % kmax # _Chai Wah Wu_, Mar 19 2022

