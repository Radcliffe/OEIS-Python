# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A366984

from math import isqrt
def A366984(n): return (-(s:=isqrt(n))*(s*(s*(s+7)+17)+17)+sum(((q:=n//w)+1)*(q*(q+5)+3*(w*(w+3)+4)) for w in range(1,s+1)))//6 # _Chai Wah Wu_, Oct 31 2023

