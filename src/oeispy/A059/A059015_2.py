# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A059015

def A059015(n): return 2+(n+1)*((t:=(n+1).bit_length())-n.bit_count())-(1<<t)-(sum((m:=1<<j)*((k:=n>>j)-(r if n<<1>=m*(r:=k<<1|1) else 0)) for j in range(1,n.bit_length()+1))>>1) # _Chai Wah Wu_, Nov 11 2024

