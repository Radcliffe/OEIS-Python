# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A246593

# implement algorithm in comment
def A246593(n):
    s = bin(n)[2:]
    s2 = s.rstrip('0')
    s3 = s2.lstrip('1')
    return(int(s2[:-len(s3)]+'1'+s3[1:-1]+'0'+s[len(s2):],2) if (len(s3) > 0 and n > 1) else n)
# _Chai Wah Wu_, Sep 08 2014

