# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A154781

def a(n):
    s = str(n)
    return sum(set(int(s[i:j]) for i in range(len(s)) for j in range(i+1, len(s)+1))) - n
print([a(n) for n in range(90)]) # _Michael S. Branicky_, Nov 08 2022

