# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A378022

def D(s):
   # D(s) returns the result of the contraction of s
   # eg. s='1244'
   contraction=False;
   mult=[0,0,0,0,0,0,0,0,0,0];
   for i in range(10):
      mult[i]=s.count(str(i));
      if mult[i]>1:contraction=True;
   if contraction==False:return '';
   r='';
   for i in range(len(s)):
      c=s[i];
      j=int(c);
      if mult[j]>1:
         r=r+str(j*mult[j]);
         mult[j]=0;
      elif mult[j]==1:r=r+c;
   return r;
# Charles Kinniburgh and Trevor Marshall, Dec 21 2019.

