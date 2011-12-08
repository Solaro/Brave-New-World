import math
def zeros(*dim):
 if len(dim) == 0:
   return 0
 row = dim[0]
 col = dim[1:]
 return [zeros(*col) for i in range(row)]

def identity(*dim):
 A=zeros(*dim)
 for i in range(len(A)):
  A[i][i]=1
 return A

def rotate(p,q,A,V=None):
 if (q<p):
  [p,q]=[q,p]
 n=len(A)
 app=A[p][p]
 aqq=A[q][q]
 apq=A[q][p]
 phi= 0.5*math.atan2(2*apq,aqq-app)
 c=math.cos(phi)
 s=math.sin(phi)
 A[p][p]=c*c*app+s*s*aqq-2*s*c*apq
 A[q][q]=s*s*app+c*c*aqq+2*s*c*apq
 A[q][p]=0
 for i in range(p):
  aip=A[p][i]
  aiq=A[q][i]
  A[p][i]=c*aip-s*aiq
  A[q][i]=c*aiq+s*aip
 for i in range(p+1,q):
  api=A[i][p]
  aiq=A[q][i]
  A[i][p]=c*api-s*aiq
  A[q][i]=c*aiq-s*api
 for i in range(q+1,n):
  api=A[i][p]
  aqi=A[i][q]
  A[i][p]=c*api-s*aqi
  A[i][q]=c*aqi+s*api
 if V!=None:
  for i in range(n):
   vip=V[p][i]
   viq=V[q][i]
   V[p][i]=c*vip-s*viq
   V[q][i]=c*viq+s*vip
 return[A,V]

def jacobi(M):
 V=identity(len(M),len(M))
 eps=1e-12
 rot=1
 A=M
 sweeps=0
 while rot==1:
  rot=0
  sweeps=sweeps+1
  for r in range(len(M)):
   for c in range(r+1,len(M)):
    if abs(A[c][r]) > eps*(abs(A[c][c])+abs(A[r][r])):
     rot=1
     [A,V]=rotate(r,c,A,V)
  
 E=[A[i][i] for i in range(len(A))]
 return [E,V,sweeps]
 
