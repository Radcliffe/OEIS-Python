# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A371808

def ok(n): return (s:=str(1<<n)).count("666") > 1 or "6666" in s
print([k for k in range(2000) if ok(k)]) # _Michael S. Branicky_, Apr 07 2024

