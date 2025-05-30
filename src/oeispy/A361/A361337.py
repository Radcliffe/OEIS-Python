# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A361337

def ok(n):
    if n < 10: return n == 0
    s = str(n)
    if "0" in s: return True
    return any(ok(int(s[:i])*int(s[i:])) for i in range(1, len(s)))
print([k for k in range(116) if ok(k)]) # _Michael S. Branicky_, Apr 02 2023

