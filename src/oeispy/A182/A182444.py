# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A182444

prpr = 0
prev = 1
for i in range(2,99):
    current = prev + (prpr % i)
    print(prpr, end=', ')
    prpr = prev
    prev = current

