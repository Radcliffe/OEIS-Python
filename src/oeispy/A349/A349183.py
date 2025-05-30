# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349183

from sympy import primefactors, prod, divisors
terms = [1]
for i in range(100):
    for j in divisors(terms[-1]):
        if j not in terms:
            terms.append(j)
            break
    else:
        terms.append(prod(primefactors(terms[-1]))*2+1)
print(terms)

