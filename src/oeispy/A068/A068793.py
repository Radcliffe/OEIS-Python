# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A068793

def A068793(n): return ((m:=n**n)*(m*(n-2)+2)-n**2+n-1)//(n-1)**2 # _Chai Wah Wu_, Mar 18 2024

