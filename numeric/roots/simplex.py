import math
def zeros(*dim):
 if len(dim) == 0:
   return 0
 row = dim[0]
 col = dim[1:]
 return [zeros(*col) for i in range(row)]

def norm(v):
 s=0
 for i in range(len(v)):
  s+=v[i]**2
 return math.sqrt(s)

def dist(a,b):
 k=[]
 for i in range(len(a)):
  k.append(a[i]-b[i])
 return norm(k)

def size(s):
 p=s[0]
 n=len(p)
 k=[]
 for i in range(len(s)-1):
  k.append(dist(s[i+1],s[0]))	
 return norm(k)



def reflect(pce,s,n):
 return [pce[i]+(pce[i]-s[h][i]) for i in range(n)]

def expand(pce,s,n):
 return [pce[i]+2*(pce[i]-s[h][i])for i in range(n)]

def contract(pce,s,n):
 return [pce[i]+0.5*(pce[i]-s[h][i]) for i in range(n)]


def simplex(fun,s,acc):
 """fun is the function to minimize and s is the starting simplex"""
 p=s[0]
 n=len(p)
 m=len(s)
 pce=zeros(n)
 fs=[]
 sos=0
 for i in range(m):
  fs.append(fun(s[i]))
 while size(s) > acc:#sos < 9:#size(s) > acc:
  #print size(s)
  sos+=1
  h=0
  l=0
  for i in range(m):
   if fs[i] > fs[h]:
    h=i
   if fs[i] < fs[l]:
    l=i
  #print h
  #print l
  #the center of gravity for P is found
  pce=zeros(n)
  for i in range(n):
    for j in range(m): 
     if j != h:
      pce[i]+=s[j][i]/n
  #print 'pce'
  #print pce
  #print 's'
  #print s
  #The reflected P is found
  pre=[pce[i]+(pce[i]-s[h][i]) for i in range(n)]
  #print 'pre'
  #print pre 
  Fre=fun(pre)
  #The expanded P
  pex=[pce[i]+2*(pce[i]-s[h][i])for i in range(n)]
  #print 'pex'
  #print pex
  if Fre < fs[h]:
   #print 'reflection accept'
   #print s
   #print 's before reflection'
   for i in range(i):
    s[h][i]=pre[i]
   fs[h]=Fre
   #print s
   #print 's after reflection'
   if Fre < fs[l]:
    Fex=fun(pex)
    if Fex < Fre: 
     #print 'extension accept'
     for i in range(n):
      s[h][i]=pex[i]
     fs[h]=Fex 
  else:
   pco=[pce[i]+0.5*(pce[i]-s[h][i]) for i in range(n)]
   #print 'pco'
   #print pco
   Fco=fun(pco)
   if Fco < fs[h]:
    #print 'contraction'
    for i in range(n):
     s[h][i]=pco[i]
    fs[h]=Fco
   else:
    #print 'reduction'

    #print s
    for i in range(m):
     if i != l:
      for k in range(n):
       #print 'hmmm'
       #print s[i][k],s[l][k]
       s[i][k]=0.5*(s[i][k]+s[l][k])
      fs[i]=fun(s[i])
    #print s
    #print 'tralala'
 return s[l]
     



