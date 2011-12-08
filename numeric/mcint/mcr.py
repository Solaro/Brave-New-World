def mcr(a,b,error,N,f,dim):
 import mc
 [y,cerror]=mc.mc(a,b,N,f,dim)
 while cerror > error: 
  x=2*x
  print x
  [y,cerror]=mc.mc(a,b,x,f,dim)
 return [y,cerror]
