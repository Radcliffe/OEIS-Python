# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A028553

n, m, A028553_list = 0, 0, []
while n < 10**12:
    s = str(m)
    if s == s[::-1]:
        A028553_list.append(n)
    m += 2*(n+2)
    n += 1 # _Chai Wah Wu_, Feb 20 2021

