# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A045926

def A045926(n):
    m = (3*n+1).bit_length()-1>>1
    return int(''.join((str(((3*n+1-(1<<(m<<1)))//(3<<((m-1-j)<<1))&3)+1) for j in range(m))))<<1 # _Chai Wah Wu_, Feb 08 2023

