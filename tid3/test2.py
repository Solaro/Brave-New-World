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
subplots_adjust(hspace=0.4)
da="centaurib.dat"#"sol.dat"
num=4000
#da="centauriA1.dat"
#da="kepler1.dat"
#da="data0.dat"
subplot(2,1,1)
[x,y,z]=opendata.opendata(data=da)
y=submean.submean(y)
for i in range(len(x)):
    y[i]=float(y[i])
    x[i]=float(x[i])*(3600*24)
    z[i]=1/float(z[i])**2
z=None
nykvist=1/(2*(x[2]-x[1]))
print nykvist
#[y,f]=aband.aband(x,y,1000,z,0.0001,0.0021,3,0.0005,0.0015)
[y]=aband.aband(x,y,z,num,0.1*nykvist,nykvist,3,3e-3,4e-3)
[f,p,a,b]=aft.aft(x,y,z,0.1*nykvist,nykvist,num)
f=multiply(1000,f)
qq=[]
uu=[]
for i in range(10,len(f)/10): 
 qq.append(auto.auto(f,p,i))
 uu.append(i*(f[2]-f[1])) 
q=0
for i in range(len(qq)):
 if qq[i] > q:
  q=qq[i]
  ii=i
print '1'
print q
print ii

plot(uu,qq)
#xlim(xmin=1, xmax=4)

ylabel('correlation')
title('Band-pass 3-4mHz Cen B')
legend()

[x,y,z]=opendata.opendata(data=da)
subplot(2,1,2)
y=submean.submean(y)
for i in range(len(x)):
    y[i]=float(y[i])
    x[i]=float(x[i])*(3600*24)
    z[i]=1/float(z[i])**2
z=None
nykvist=1/(2*(x[2]-x[1]))
print nykvist
#[y,f]=aband.aband(x,y,1000,z,0.0001,0.0021,3,0.0005,0.0015)
[y]=aband.aband(x,y,z,num,0.1*nykvist,nykvist,3,4e-3,5e-3)
[f,p,a,b]=aft.aft(x,y,z,0.1*nykvist,nykvist,num)
f=multiply(1000,f)
qq=[]
uu=[]
for i in range(10,len(f)/10): 
 qq.append(auto.auto(f,p,i))
 uu.append(i*(f[2]-f[1])) 
q=0
for i in range(len(qq)):
 if qq[i] > q:
  q=qq[i]
  ii=i
print '2'
print q
print ii

plot(uu,qq)
#xlim(xmin=1, xmax=4)

ylabel('correlation')
title('Band-pass 4-5mHz Cen B')
legend()
savefig('CenBcor.ps')
show()

