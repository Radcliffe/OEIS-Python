# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A052024

from sympy import isprime
from itertools import count, islice
def agen(verbose=False):
    prime_strings, alst = {"3", "7"}, []
    yield from [2, 3, 5, 7]
    for digs in count(2):
        new_prime_strings = set()
        for p in prime_strings:
            for d in "123456789":
                ts = d + "0"*(digs-1-len(p)) + p
                if isprime(int(ts)):
                    new_prime_strings.add(ts)
        prime_strings |= new_prime_strings
        pals = [int(s) for s in new_prime_strings if s == s[::-1]]
        yield from sorted(pals)
        if verbose: print("...", digs, len(prime_strings), time()-time0)
print(list(islice(agen(), 20))) # _Michael S. Branicky_, Apr 04 2022

