#Numerical integration Implement an recursive adaptive integrator which estimates the integral with a required absolute (acc) and relative (eps) accuracy. 

import math
def adp(a,b,acc,eps,f,op=None):
 x=[float(1)/6,float(2)/6,float(4)/6,float(5)/6] #abscissas
 w=[float(2)/6,float(1)/6,float(1)/6,float(2)/6] #higher order weights
 v=[float(1)/2,float(1)/2,float(1)/2,float(1)/2] #lower order weights
 p=[1,0,0,1]
 n=len(x)
 h=b-a
 fs=[]
 if op == None:
  for i in range(n):
   fs.append(f.f(a+x[i]*h))
 else:
  k=0
  for i in range(len(x)):
   if p[i]==1:
    fs[i]=f.f(a+x[i]*h)
   else:
    fs[i]=op[k]
    k=k+1  
 q4=0
 q2=0
 for j in range(n):
  q4+=w[j]*fs[j]*float(h)
  q2+=v[j]*fs[j]*float(h)/2
 tol=acc+eps*abs(q4)
 err=abs(q4-q2)
 if (err<tol):
  return [q4,err]
 else:
  acc/=math.sqrt(2)
  mid=float(a+b)/2
  for i in range(n):
   if i < 2:
    left=fs[i]
   else:
    right=fs[i] 
  [ql,el]=adp(a,mid,eps,acc,f,op)
  [qr,er]=adp(mid,b,eps,acc,f,op)
  return [ql+qr, math.sqrt(el**2+er**2)]
