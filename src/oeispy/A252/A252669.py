# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A252669

import math
for n in range(1,333):
    res=-1
    for k in range(2**31-1):
        if ((n*k) % (n+k) == 1):
            res=k
            break
    print(res, end=', ')

