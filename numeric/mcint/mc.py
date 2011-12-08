#montecarlo one dimensional
def randomx(a,b,dim):
 import random
 u=[]
 for i in range(dim):
  u.append(a[i]+random.random()*(b[i]-a[i])) 
 return u
def mc(a,b,N,f,dim): 
 import math
 V=[]
 for i in range(dim):
  V.append(b[i]-a[i]) 
 sum=0
 sum2=0
 Vo=1
 for i in range(N):
  k=f.f(randomx(a,b,dim))
  sum+=k
  sum2+=k**2
 average=sum/N
 variance=sum2/N-average**2
 for i in range(dim):
  Vo*=V[i]
 integral=Vo*average
 error=Vo*math.sqrt(variance/N)
 return [integral,error]  
