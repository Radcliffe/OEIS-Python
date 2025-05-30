# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A327971

def A269160(n): return(n^((n<<1)|(n<<2)))
def A269161(n): return((n<<2)^((n<<1)|n))
def genA327971():
    '''Yield successive terms of A327971.'''
    s1 = 1
    s2 = 1
    while True:
       yield (s1^s2)
       s1 = A269160(s1)
       s2 = A269161(s2)

