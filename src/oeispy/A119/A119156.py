# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A119156

klimit = 10**6
A000217 = (k*(k+1)//2 for k in range(klimit)) # generator
print([m for m in A000217 if set(str(m)) <= set("238")]) # _Michael S. Branicky_, Mar 28 2021

