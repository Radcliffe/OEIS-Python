# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A348570

# Using functions NumToFib and RevFibToNum from A349238.
n, a = 0, 0
while n < 53:
    a += 1
    aa, sa = a, NumToFib(a)
    ar, s = RevFibToNum(sa), 0
    while aa != ar and s < 10000:
        s, aa = s+1, aa+ar
        sa = NumToFib(aa)
        ar = RevFibToNum(sa)
    if aa != ar:
        n += 1
        print(a, end = ", ")

