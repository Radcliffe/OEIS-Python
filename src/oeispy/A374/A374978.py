# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A374978

from sympy import divisor_sigma
def A374978(n): return sum(divisor_sigma(j)*sum((5*divisor_sigma(i+1,3)-(5+6*i)*divisor_sigma(i+1))*(5*divisor_sigma(n-j-i-1,3)-(5+6*(n-j-i-2))*divisor_sigma(n-j-i-1)) for i in range(1,n-j-2)) for j in range(1,n))//144

