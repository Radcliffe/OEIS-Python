# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A366937

from math import isqrt
def A366937(n): return (((s:=isqrt(m:=n>>1))*(s+1)**2*((s<<2)+5)<<1)-(t:=isqrt(n))*(t+1)**2*(t+2)-sum((((q:=m//w)+1)*(q*((q<<2)+5)+6*w*((w<<1)+1))<<1) for w in range(1,s+1))+sum(((q:=n//w)+1)*(q*(q+2)+3*w*(w+1)) for w in range(1,t+1)))//6 # _Chai Wah Wu_, Oct 29 2023

