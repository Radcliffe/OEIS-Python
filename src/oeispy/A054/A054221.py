# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A054221

# Algorithm without multiplications nor divisions.
n=0; i=0; T_i=0
while i<100000:
  j=i; i+=1; k=1; kd2=1; kd3=0; T_j=T_i; delta=T_j+j; T_i+=i;
  while j>0:
    if delta>0:
      kd3+=6; kd2+=kd3; delta-=kd2; k+=1;
    else:
      if delta==0:
        print("A054221(%d)= %d, A054222(%d)= %d, A054223(%d)= %d"%
              (n,i,n,j,n,k)); n+=1;
      delta += T_j; T_j-=j; j-=1;
# _Bert Dobbelaere_, Jan 14 2019

