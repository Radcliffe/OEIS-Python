# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A339771

def A339771():
    a, b, c = 1, 7, 27
    yield(a); yield(b)
    while True:
        yield c
        z = 4*a - 8*b + 5*c
        a, b, c = b, c, z
a = A339771()
print([next(a) for _ in range(30)]) # _Peter Luschny_, Dec 17 2020

