# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A018796

n = 1
while n < 100:
    for k in range(10**3):
        if str(k**2).startswith(str(n)):
            print(k**2,end=', ')
            break
    n += 1 # _Derek Orr_, Jul 31 2014

