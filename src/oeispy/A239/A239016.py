# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A239016

def ok(n):
    s = str(n)
    if "".join(sorted(s)) == s: return True
    return all(n <= int(s[i:] + s[:i]) for i in range(1, len(s)))
print(list(filter(ok, range(133)))) # _Michael S. Branicky_, Aug 21 2021

