# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A003714

def fibbinary():
    x = 0
    while True:
        yield x
        y = ~(x >> 1)
        x = (x - y) & y # _Falk Hüffner_, Oct 23 2021

