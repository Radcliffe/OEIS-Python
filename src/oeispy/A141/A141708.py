# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A141708

def binpal(n): b = bin(n)[2:]; return b == b[::-1]
def a(n):
    m = 2*n - 1
    km = m
    while not binpal(km): km += m
    return km
print([a(n) for n in range(1, 55)]) # _Michael S. Branicky_, Mar 20 2022

