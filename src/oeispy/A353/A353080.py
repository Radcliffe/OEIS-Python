# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A353080

def ok(n): s = str(n**2); return len(s) > 5 and s[:3] == s[3:6]
print([k for k in range(20000) if ok(k)]) # _Michael S. Branicky_, Apr 22 2022

