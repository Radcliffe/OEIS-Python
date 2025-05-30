# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A256481

from gmpy2 import mpz, digits, is_prime
def A256481(n,limit=2000):
    if n in (6930,50358,56574,72975):
        return 0
    if n == 0:
        return 2
    sn = str(n)
    for i in range(1,limit+1):
        for j in range(1,10,2):
            si = digits(j,10)*i
            p = mpz(sn+si)
            if is_prime(p):
                return int(p)
    else:
        return 'search limit reached.'

