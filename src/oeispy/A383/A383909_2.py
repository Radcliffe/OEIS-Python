# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A383909

def A383909(n):
    s = ('0' if n.bit_length()&1 else '')+bin(n)[2:] if n else '00'
    return int(''.join(('1000','1001','1100','1101')[int(s[i:i+2],2)] for i in range(0,len(s),2)),2) # _Chai Wah Wu_, May 22 2025

