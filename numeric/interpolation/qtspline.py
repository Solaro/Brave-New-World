
def eeval(x,y,z):
 a=len(x)/2
 i=0
 j=len(x)
 while (j-i)>1:
  if(z>x[a]):
   i=a
  else:
   j=a
  a=(i+j)/2
 return [i,j] 


def pinterp(x,y,z,k=None):
 if k==None:
  s=0
  for i in range(len(x)):
   p=1
   for k in range(len(x)):
    if k!=i:
     p*=(z-x[k])/(x[i]-x[k])
   s+=y[i]*p
  return [s]
 else:
  s=0
  a=int((len(x)-k)/2)
  for i in range(k):
   p=1
   for k in range(k):
    if k!=i:
     p*=(z-x[a+k])/(x[a+i]-x[a+k])
   s+=y[a+i]*p
  return [s]


def linterpol(x,y,antal=None):
 if antal==None:
  antal=2*len(x)
 S=[]
 k=[x[0]+(x[len(x)-1]-x[0])*i/(antal-1) for i in range(antal)]
 for z in k:
  [a,b]=eeval(x,y,z)
  w=y[b]+float(y[a]-y[b])/float(x[a]-x[b])*(z-x[b])
  S.append(w)
 return [k,S]

def qinterpol(x,y,antal=None):
 if antal==None:
  antal=2*len(x)
 qa=qs(x,y)
 S=[]
 k=[x[0]+(x[len(x)-1]-x[0])*i/(antal-1) for i in range(antal)]
 for z in k:
  [a,b]=eeval(x,y,z)
  w=y[b]+float(y[a]-y[b])/float(x[a]-x[b])*(z-x[b])+qa[a]*float(z-x[b])*float(z-x[a])
  S.append(w)
 return [k,S]

def qs(x,y):
 a1=[]
 ha=0 
 a1.append(ha)
 for i in range(len(x)-2):   
  ha=1.0/float(x[i+2]-x[i+1])*(float(y[i+2]-y[i+1])/(x[i+2]-x[i+1])-float(y[i+1]-y[i])/(x[i+1]-x[i])-ha*(x[i+1]-x[i]))
  a1.append(ha)
 return a1


