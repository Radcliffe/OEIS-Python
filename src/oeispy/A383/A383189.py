# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A383189

def A383189(n):
    if not hasattr(A:=A383189, 'terms'): A.terms=[0]
    while len(t := A.terms) <= n:
       try: any(t.append(A383187.terms.index(k))for k in range(len(t), n+1))
       except: A383187(len(getattr(A383187,'terms',0)+100))
    return A.terms[n]

