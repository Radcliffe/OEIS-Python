# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A046260

def c(s): return s[0] != "0" and s == s[::-1]
def a(n):
    s = str(2**n)
    ss = (s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1))
    return max(int(w) for w in ss if c(w))
print([a(n) for n in range(62)]) # _Michael S. Branicky_, Sep 18 2022

