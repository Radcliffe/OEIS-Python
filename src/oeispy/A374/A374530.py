# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A374530

from itertools import count
a = [0]
while len(a) < 30: a.append(next(k for k in count() if k not in a and ((r:=a[-1]%10)==(l:=int(str(k)[0])) or ((r,l)==(0,1)))))
print(a) # _Dominic McCarty_, Mar 24 2025

