# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A383183

from sympy import isprime # = A010051
def square_number(z): return int(4*y**2-y-x if (y := z.imag) >= abs(x := z.real)
    else 4*x**2-x-y if -x>=abs(y) else (4*y-3)*y+x if -y>=abs(x) else (4*x-3)*x+y)
def A383183(n, moves=(1, 1+1j, 1j, 1j-1, -1, -1-1j, -1j, 1-1j)):
    if not hasattr(A:=A383183, 'terms'): A.terms=[0]; A.pos=0; A.path=[0]
    while len(A.terms) <= n:
        try: _,s,z = min((1-isprime(s), s, z) for d in moves if
                     (s := square_number(z := A.pos+d)) not in A.terms)
        except ValueError:
            raise IndexError(f"Sequence has only {len(A.terms)} terms")
        A.terms.append(s); A.pos = z; A.path.append(z)
    return A.terms[n]
A383183(999) # gives IndexError: Sequence has only 172 terms
A383183.terms # shows the full sequence; append [:N] to show only N terms
import matplotlib.pyplot as plt # this and following to plot the path:
plt.plot([z.real for z in A383183.path], [z.imag for z in A383183.path])
plt.show()

