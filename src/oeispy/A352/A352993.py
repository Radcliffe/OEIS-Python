# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A352993

def a(n):
    b = bin(n)[2:][::-1]
    z = [k for k, bk in enumerate(b+'0'*(len(b)-b.count('0'))) if bk=='0']
    return sum(int(bk)*2**zk for bk, zk in zip(b, z))
print([a(n) for n in range(56)]) # _Michael S. Branicky_, Apr 21 2022

