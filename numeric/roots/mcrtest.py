def mcrtest(a,b,error,f,dim):
 import mc
 N=500
 [y,cerror]=mc.mc(a,b,N,f,dim)
 while cerror > error: 
  x=2*x
  print x
  [y,cerror]=mc.mc(a,b,x,f,dim)
 return [y,cerror]
