# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A249032

def A249032(n): return 4+int((n+1|(~((m:=n>>1)+1)&m).bit_length())&1^1)+int((n|(~((k:=n-1>>1)+1)&k).bit_length())&1) if n else 3 # _Chai Wah Wu_, Sep 11 2024

