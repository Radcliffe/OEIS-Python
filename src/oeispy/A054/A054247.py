# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A054247

def a(n):
    return 2**(n**2-3)+2**((n**2-8)/4)+2**((n**2-6)/2)+2**((n**2-4)/2)+2**((n**2+n-4)/2) if n % 2 == 0 else 2**(n**2-3)+2**((n**2-5)/4)+2**((n**2-5)/2)+2**((n**2+n-2)//2) # _Peter E. Francis_, Apr 12 2020

