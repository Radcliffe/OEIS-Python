# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A333599

def a(n):
    f1 = 0
    f2 = 1
    for i in range(n):
        f = f1 + f2
        f1 = f2
        f2 = f
    return (f1 * f2) % (f1 + f2)

