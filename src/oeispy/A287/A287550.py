# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A287550

from gmpy2 import is_prime, next_prime
A287550_list, p = [], 2
q, r, s = p+72, p+144, p+216
while s <= 10**10:
    np = next_prime(p)
    if np == q and is_prime(r) and is_prime(s) and next_prime(q) == r and next_prime(r) == s:
        A287550_list.append(p)
    p, q, r, s = np, np+72, np+144, np+216 # _Chai Wah Wu_, Jun 03 2017

