# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A048344

A048344_list = []
for n in range(1,10**5):
    s = str(n)
    s2 = str(n)[::-1]
    if s != s2:
        s3 = str(n*int(s2))
        if s3 == s3[::-1]:
            A048344_list.append(n) # _Chai Wah Wu_, Sep 08 2014

