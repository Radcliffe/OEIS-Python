# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A189823

def rchampernowne(n):
    stri=''
    for i in range(1,n+1) :
        if stri.count(str(i))==0 : stri=stri+str(i)
    return '0.'+stri+'...'
print(rchampernowne(100)) # computes the decimal representation of the reduced Champernowne number until step 100 is reached. The computation of rchampernowne(n) ends when step n is reached, not when n appears in the decimal representation.

