# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A256786

primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
def ok(n):
    s = str(n)
    return "0" not in s and all(n%primes[int(d)] == 0 for d in s)
print([k for k in range(22213) if ok(k)]) # _Michael S. Branicky_, Dec 14 2021

