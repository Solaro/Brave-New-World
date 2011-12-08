import math
def trans(A):
 a=len(A)
 b=len(A[0])
 At=zeros(b,a)
 for i in range(b):
  for j in range(a):
   At[i][j]=A[j][i]
 return At

def ttimes(A,B):
 #calculates the dotproduct between A transposed and B
 At=trans(A)
 Bt=trans(B)
 a=len(At)
 b=len(B[0]) 
 D=zeros(a,b)
 x=0
 for i in At:
  y=0
  for j in Bt:
   D[x][y]=dot(i,j)
   y=y+1
  x=x+1
 return D
 

def inv(A):
 [Q,R]=qrdec(A)
 a=len(A)
 Ai=zeros(a,a)
 for i in range(a):
   b=zeros(a)
   b[i]=1
   x=qrback(Q,R,b)
   for k in range(a):
    Ai[i][k]=x[k]
 return Ai


def dot(a,b):
 s=0
 for i in range(len(a)):
  s+=a[i]*b[i]
 return s 

def qrback(Q,R,b):
 m=len(Q)
 c=[0]*m
 x=[0]*m
 for i in range(m):
  for k in range(len(b)):
   c[i]+=Q[i][k]*b[k]
  for ii in range(m):
   i=(m-1)-ii
   s=0
   for k in range(i+1,m):
    s+=R[k][i]*x[k]
   x[i]=(c[i]-s)/R[i][i]
 return x

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

def zeros(*dim):
 if len(dim) == 0:
   return 0
 row = dim[0]
 col = dim[1:]
 return [zeros(*col) for i in range(row)]

def lsfit(x,y,dy,funs):
 #datapoints {x,y,dy} where dy is sigma
 #funs is the function that has to fitted to
 #a=len(x)
 #b=len(funs)
 b=[]
 A=zeros(len(funs),len(x))
 for i in range(len(x)):
  for j in range(len(funs)):
   A[j][i]=funs[j](x[i])/dy[i]
 for i in range(len(y)):
  b.append(float(y[i])/dy[i])
 [Q,R]=qrdec(A)
 c=qrback(Q,R,b)
 S=inv(ttimes(R,R))
 return [c,S]
