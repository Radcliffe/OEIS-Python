# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A366985

from math import isqrt
def A366985(n): return (-(s:=isqrt(n))*(s*(s*(s*(s+11)+45)+85)+74)+sum(((q:=n//w)+1)*(q*(q*(q+9)+26)+((w+4)*(w*(w+2)+3)<<2)) for w in range(1,s+1)))//3>>3 # _Chai Wah Wu_, Oct 31 2023

