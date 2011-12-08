import math
def norm(v):
 s=0
 for i in range(len(v)):
  s+=v[i]**2
 return math.sqrt(s)

def zeros(*dim):
 if len(dim) == 0:
   return 0
 row = dim[0]
 col = dim[1:]
 return [zeros(*col) for i in range(row)]

def dot(a,b):
 s=0
 for i in range(len(a)):
  s+=a[i]*b[i]
 return s 
def qrdec(A):
 m=len(A)
 Q=A
 R=zeros(m,m)
 for i in range(m):
  e=Q[i]
  r=math.sqrt(dot(e,e))
  if r == 0:
   print 'singular matrix'
  R[i][i]=r
  for k in range(len(e)):
   e[k]/=r
  for j in range(i+1,m):
   q=Q[j]
   s=dot(e,q)
   for k in range(len(q)):
    q[k]-=s*e[k]
   R[j][i]=s  
 return [Q,R]

def qrback(Q,R,b):
 m=len(Q)
 c=[0]*m
 x=[0]*m
 for i in range(m):
  for k in range(len(b)):
   c[i]+=Q[i][k]*b[k]
  for ii in range(m):
   i=m-1-ii
   s=0
   for k in range(i+1,m):
    s+=R[k][i]*x[k]
   x[i]=(c[i]-s)/R[i][i]
 return x

def newton(fs,x,acc=None,dx=None):
 if acc==None:
  acc=1e-6
 if dx==None:
  dx=1e-8
 a=len(x)
 s=0.01
 J=zeros(a,a)
 minusfx=zeros(a)
 minusfz=zeros(a)
 z=zeros(a)
 for i in range(a):
  minusfx[i]=-fs[i](x)
 while (norm(minusfx)>acc):   
  for i in range(a):
   for k in range(a):
    x[k]+=dx
    J[k][i]=(fs[i](x)+minusfx[i])/dx
    x[k]-=dx
  [Q,R]=qrdec(J)
  Dx=qrback(Q,R,minusfx)
#  print Dx
#  return norm(minusfz),norm(minusfx)
  for i in range(a):
   z[i]=x[i]+s*Dx[i]
  for i in range(a):
   minusfz[i]=-fs[i](z)
  while ((1-s/2)*norm(minusfz)>norm(minusfx) and s>float(1)/128):
   s=float(s)/2
   for i in range(a):
    z[i]=x[i]+s*Dx[i]
   for i in range(a):
    minusfz[i]=-fs[i](z)
  minusfx=minusfz[:] 
  x=z
  #print z
 return z
