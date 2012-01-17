#powerspektret er givet som p=a**2+b**2
import math
from numpy import *
def aft(x,y,z=None,fmin=None,fmax=None,antal=None):
 #antag at filerne er importeren og ligger som x[i],y[i] hvor x[i]-angiver tiden
 if fmin==None:
  fmin=0.01
 if fmax==None:
  fmax=100
 if antal==None:
  antal=1000
 #antal=(fmax-fmin)/oplosning
 p=[]
 frek=[]
 a=[]
 b=[]
 xx=[]
 yy=[]
 zz=[]
 if z==None:
    for i in range(len(x)):
         xx.append(float(x[i]))
         yy.append(float(y[i]))
    for f in range(antal):
        f=fmin+(fmax-fmin)*float(f)/(antal)
        f=2*pi*f
        #for at skifte til vinkelfrekvens
        fx=multiply(f,x)
        s=0
        c=0
        ss=0
        cc=0
        sc=0
        s=dot(y,sin(fx))
        c=dot(y,cos(fx))
        ss=dot(sin(fx),sin(fx))
        cc=dot(cos(fx),cos(fx))
        sc=dot(cos(fx),sin(fx))
        aa=(s*cc-c*sc)/(ss*cc-sc**2)
        bb=(c*ss-s*sc)/(ss*cc-sc**2)
        a.append(aa)
        b.append(bb)
        p.append(aa**2+bb**2)
        f=f/(2*math.pi)
        frek.append(f)
    return [frek,p,a,b]
 else:
     for i in range(len(x)):
         xx.append(float(x[i]))
         yy.append(float(y[i]))
         zz.append(float(z[i]))
     for f in range(antal):
        f=fmin+(fmax-fmin)*float(f)/(antal)
        f=2*math.pi*f
        #for at skifte til vinkelfrekvens
        s=0
        c=0
        ss=0
        cc=0
        sc=0
        fx=multiply(f,x)
        wy=multiply(zz,yy)
        s=dot(wy,sin(fx))
        c=dot(wy,cos(fx))
        ss=dot(zz,multiply(sin(fx),sin(fx)))
        cc=dot(zz,multiply(cos(fx),cos(fx)))
        sc=dot(zz,multiply(cos(fx),sin(fx)))
        aa=(s*cc-c*sc)/(ss*cc-sc**2)
        bb=(c*ss-s*sc)/(ss*cc-sc**2)
        a.append(aa)
        b.append(bb)
        p.append(aa**2+bb**2)
        f=f/(2*math.pi)
        frek.append(f)
     return [frek,p,a,b]
