# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A364834

sn = lambda k, n: ((n // k)*((n // k) + 1) * k) // 2
a = lambda n: sn(2, n) + sn(5, n) - sn(10, n)
print([a(n) for n in range(1, 56)])

