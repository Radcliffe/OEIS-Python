# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A309092

from re import split
from sympy import isprime
seq_list, n = [],1
while len(seq_list) < 10000:
    for d in split('[1-9]+|[a-f]+', format(n,'x')):
        if isprime(len(d)):
            seq_list.append(n)
    n += 1

