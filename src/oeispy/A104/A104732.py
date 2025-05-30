# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A104732

def A104732_rows(n):
    """Produces n rows of A104732 triangle"""
    from operator import iadd
    a,b,c = [], [1], [1]
    for i in range(2,n+1):
            a,b = b, [i]+list(map(iadd,a,b[:-1]))+[1]
            c+=b
    return c
# Alec Mihailovs (alec(AT)mihailovs.com), May 04 2008

