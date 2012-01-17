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
da="sol.dat"
num=5000
#da="centauriA1.dat"
#da="kepler1.dat"
#da="data0.dat"
[x,y,z]=opendata.opendata(data=da)
y=submean.submean(y)
for i in range(len(x)):
    y[i]=float(y[i])
    x[i]=float(x[i])#*(3600)
#    z[i]=1/float(z[i])**2
z=None
nykvist=1/(2*(x[2]-x[1]))
print nykvist
#[y,f]=aband.aband(x,y,1000,z,0.0001,0.0021,3,0.0005,0.0015)
#[y]=aband.aband(x,y,z,num,0.1*nykvist,nykvist,2,0.4*nykvist,0.4*nykvist)
[f,p,a,b]=aft.aft(x,y,z,0.1*nykvist,nykvist,num)
f=multiply(1000,f)
subplot(3,1)


plot(p,f)
ylabel('correlation')
title('Low-pass 0.1-0.4 $f_{nykvist}$ Sun')
legend()

[x,y,z]=opendata.opendata(data=da)
y=submean.submean(y)
for i in range(len(x)):
    y[i]=float(y[i])
    x[i]=float(x[i])#*(3600)
#    z[i]=1/float(z[i])**2
z=None
nykvist=1/(2*(x[2]-x[1]))
print nykvist
#[y,f]=aband.aband(x,y,1000,z,0.0001,0.0021,3,0.0005,0.0015)
#[y]=aband.aband(x,y,z,num,0.1*nykvist,nykvist,2,0.4*nykvist,0.7*nykvist)
[f,p,a,b]=aft.aft(x,y,z,0.1*nykvist,nykvist,num)
f=multiply(1000,f)
subplot(3,2)

qq=[]
uu=[]

plot(p,f)
ylabel('correlation')
title('Band-pass 0.4-0.7 $f_{nykvist}$ Sun')
legend()

[x,y,z]=opendata.opendata(data=da)
y=submean.submean(y)
for i in range(len(x)):
    y[i]=float(y[i])
    x[i]=float(x[i])#*(3600)
#    z[i]=1/float(z[i])**2
z=None
nykvist=1/(2*(x[2]-x[1]))
print nykvist
#[y,f]=aband.aband(x,y,1000,z,0.0001,0.0021,3,0.0005,0.0015)
#[y]=aband.aband(x,y,z,num,0.1*nykvist,nykvist,1,0.7*nykvist,0.7*nykvist)
[f,p,a,b]=aft.aft(x,y,z,0.1*nykvist,nykvist,num)
f=multiply(1000,f)
subplot(3,3)


plot(p,f)
ylabel('correlation')
title('High-pass 0.7-1 $f_{nykvist}$ Sun')
legend()

show()
