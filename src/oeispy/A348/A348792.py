# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A348792

from sympy import isprime
def afind(limit):
    s, k = "", 1
    for k in range(1, limit+1):
        s += bin(k)[2:][::-1]
        t = int(s[::-1], 2)
        if isprime(t):
            print(k, end=", ")
afind(200) # _Michael S. Branicky_, Dec 03 2021

