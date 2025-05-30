# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A154694

from sage.all import *
from sage.combinat.combinat import eulerian_number
def A154694(n,k): return (pow(2,n-k)*pow(3,k)+pow(2,k)*pow(3,n-k))*eulerian_number(n+1,k)
print(flatten([[A154694(n,k) for k in range(n+1)] for n in range(13)])) # _G. C. Greubel_, Jan 18 2025

