# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A174605

def A174605(n): return (n*(n+1)>>1)-(n+1)*n.bit_count()-(sum((m:=1<<j)*((k:=n>>j)-(r if n<<1>=m*(r:=k<<1|1) else 0)) for j in range(1,n.bit_length()+1))>>1)  # _Chai Wah Wu_, Nov 12 2024

