# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A206481

prpr = 0
prev = 1
for n in range(1,77):
    print(prpr, end=',')
    curr = n*n*n - prpr    # a(n+1)
    prpr = prev
    prev = curr

