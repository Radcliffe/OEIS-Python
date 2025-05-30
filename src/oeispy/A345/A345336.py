# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A345336

from numbthy import isprime
counter = 1
for p in range (2,1090821):
    if isprime(p) and (counter <= 10000):
        pp_product = 1
        pp_sum = 0
        for digit in range (0, len(str(p*p))):
            pp_product *= int(str(p*p)[digit])
            pp_sum += int(str(p*p)[digit])
        if pow(int(pp_product**0.5),2) == pp_product:
            if pow(int(pp_sum**0.5),2) == pp_sum:
                print(counter, p)
                counter += 1; # _Karl-Heinz Hofmann_, Jun 17 2021

