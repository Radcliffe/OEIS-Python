# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376946

from sympy import isprime, prevprime
def A(n):
    m = 3**(4*3**n)
    p = prevprime(m)
    while not isprime((p-1)//2):
        p = prevprime(p)
    return m-p #

