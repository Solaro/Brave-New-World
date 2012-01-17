import math
import aft
from numpy import *

def aclean(x,y,z=None,fmin=None,fmax=None,antal=None,cantal=None,fclean=None):
 if cantal==None:
  cantal=1
 if fclean==None:
  fclean=[]
  pclean=[]
 while cantal > 0:
  q=0
  ii=0
  [f,p,a,b]=aft.aft(x,y,z,fmin,fmax,antal)
  for i in range(len(p)):
   if p[i] > q:
    q=p[i]
    ii=i
  fclean.append(f[ii])
  pclean.append(p[ii])
  y=subtract(y,(multiply(a[ii],sin(multiply(2*pi*f[ii],x)))+multiply(b[ii],cos(multiply(2*pi*f[ii],x)))))
  cantal=cantal-1
 return [y,fclean,pclean] 
