# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A120433

def ok(n): return {"4", "9"} & set(str(n))
afull = [k for k in range(4000) if ok(k)] # _Michael S. Branicky_, Aug 20 2024

