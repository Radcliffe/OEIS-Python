# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A377279

def f(b):
    count = 0
    for n in range(b*b):
        val = ((n*n) // b) % (b*b)
        if n == val:
            count += 1
    return count

