# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A241490

def zeroless():
    yield from range(1, 10)
    for z in zeroless():
        yield from range(10*z + 1, 10*z + 10)
def A241490(n):
    return next(z for z in zeroless() if str(z*z*z).count('0') == n)
# _David Radcliffe_, Jun 25 2025

