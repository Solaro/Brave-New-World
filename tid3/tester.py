#script der tager data og analyserer dem.


import opendata
import aft
import submean
from pylab import *
from numpy import *
import aband
import aclean
import awindow
import auto
import bins
subplots_adjust(hspace=0.4)
da="centaurib.dat"#"sol.dat"
num=4000
#da="centauriA1.dat"
#da="kepler1.dat"
#da="data0.dat"
subplot(3,1,1)
[x,y,z]=opendata.opendata(data=da)
y=submean.submean(y)
for i in range(len(x)):
    y[i]=float(y[i])
    x[i]=float(x[i])*(3600*24)
    z[i]=1/float(z[i])**2
z=None
nykvist=1/(2*(x[2]-x[1]))
print len(x)
#[y,f]=aband.aband(x,y,1000,z,0.0001,0.0021,3,0.0005,0.0015)
#[y]=aband.aband(x,y,z,num,0.1*nykvist,nykvist,3,2.5e-3,4.6e-3)
[f,p,a,b]=aft.aft(x,y,z,0.1*nykvist,nykvist,num)
f=multiply(1000,f)
qq=[]
uu=[]
for i in range(10,len(f)/10): 
 qq.append(auto.auto(f,p,i))
 uu.append(i*(f[2]-f[1])) 
plot(f,p)
#xlim(xmin=1, xmax=4)
q=0
for i in range(len(qq)):
 if qq[i] > q:
  q=qq[i]
  ii=i
print q
print ii
ylabel('correlation')
title('sun')
legend()
savefig('sun1cor.ps')
show()

