# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A249951

from sympy import isprime
A249951_list, m = [], [362880, -1229760, 1607760, -1011480, 309816, -40752, 1584, -4, 1]
for n in range(1,10**5+1):
    for i in range(8):
        m[i+1]+= m[i]
    if isprime(m[-1]):
        A249951_list.append(n)

