# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A129623

# instantly generates 44185 terms with n = 5
def aupto2ndigits(n): return(sorted(set(i*int(s[::-1]) for i in range(12, 10**n) if i%10 != 0 and (s:=str(i)) != s[::-1])))
print(aupto2ndigits(2))
# _Michael S. Branicky_, Sep 08 2024 after _Hans Rudolf Widmer_

