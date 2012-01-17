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
[y]=aband.aband(x,y,z,num,0.1*nykvist,nykvist,2,0.4*nykvist,0.4*nykvist)
[f,p,a,b]=aft.aft(x,y,z,0.1*nykvist,nykvist,num)
f=multiply(1000,f)
subplot(3,3,1)

qq=[]
uu=[]
for i in range(10,len(f)/10): 
 qq.append(auto.auto(f,p,i))
 uu.append(i*(f[2]-f[1])) 


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
#[y,f]=aband.aband(x,y,1000,z,0.0001,0.0021,3,0.0005,0.0015
[y]=aband.aband(x,y,z,num,0.1*nykvist,nykvist,2,0.4*nykvist,0.7*nykvist)
[f,p,a,b]=aft.aft(x,y,z,0.1*nykvist,nykvist,num)
f=multiply(1000,f)
subplot(3,3,2)

qq=[]
uu=[]
for i in range(10,len(f)/10): 
 qq.append(auto.auto(f,p,i))
 uu.append(i*(f[2]-f[1])) 


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
[y]=aband.aband(x,y,z,num,0.1*nykvist,nykvist,1,0.7*nykvist,0.7*nykvist)
[f,p,a,b]=aft.aft(x,y,z,0.1*nykvist,nykvist,num)
f=multiply(1000,f)
subplot(3,3,3)

qq=[]
uu=[]
for i in range(10,len(f)/10): 
 qq.append(auto.auto(f,p,i))
 uu.append(i*(f[2]-f[1])) 


plot(uu,qq)
ylabel('correlation')
title('High-pass 0.7-1 $f_{nykvist}$ Sun')
legend()

show()

#----------------------------------------------------------------------
da="centauria.dat"
#da="centauriA1.dat"
#da="kepler1.dat"
#da="data0.dat"
[x,y,z]=opendata.opendata(data=da)
y=submean.submean(y)
for i in range(len(x)):
    y[i]=float(y[i])
    x[i]=float(x[i])#*(3600)
    z[i]=1/float(z[i])**2

nykvist=1/(2*(x[2]-x[1]))
print nykvist
[y]=aband.aband(x,y,z,num,0.1*nykvist,nykvist,2,0.4*nykvist,0.4*nykvist)
[f,p,a,b]=aft.aft(x,y,z,0.1*nykvist,nykvist,num)
f=multiply(1000,f)
subplot(3,3,4)
qq=[]
uu=[]
for i in range(10,len(f)/10): 
 qq.append(auto.auto(f,p,i))
 uu.append(i*(f[2]-f[1])) 

plot(uu,qq)
title('Low-pass 0.1-0.4 $f_{nykvist}$ Cen A')
ylabel('correlation')
legend()

[x,y,z]=opendata.opendata(data=da)
y=submean.submean(y)
for i in range(len(x)):
    y[i]=float(y[i])
    x[i]=float(x[i])#*(3600)
    z[i]=1/float(z[i])**2

nykvist=1/(2*(x[2]-x[1]))
print nykvist
[y]=aband.aband(x,y,z,num,0.1*nykvist,nykvist,3,0.4*nykvist,0.7*nykvist)
[f,p,a,b]=aft.aft(x,y,z,0.1*nykvist,nykvist,num)
f=multiply(1000,f)
subplot(3,3,5)
qq=[]
uu=[]
for i in range(10,len(f)/10): 
 qq.append(auto.auto(f,p,i))
 uu.append(i*(f[2]-f[1])) 

plot(uu,qq)
title('Band-pass 0.4-0.7 $f_{nykvist}$ Cen A')
ylabel('correlation')
legend()

[x,y,z]=opendata.opendata(data=da)
y=submean.submean(y)
for i in range(len(x)):
    y[i]=float(y[i])
    x[i]=float(x[i])#*(3600)
    z[i]=1/float(z[i])**2

nykvist=1/(2*(x[2]-x[1]))
print nykvist
[y]=aband.aband(x,y,z,num,0.1*nykvist,nykvist,1,0.7*nykvist,0.7*nykvist)
[f,p,a,b]=aft.aft(x,y,z,0.1*nykvist,nykvist,num)
f=multiply(1000,f)
subplot(3,3,6)
qq=[]
uu=[]
for i in range(10,len(f)/10): 
 qq.append(auto.auto(f,p,i))
 uu.append(i*(f[2]-f[1])) 

plot(uu,qq)
title('High-pass 0.7-1 $f_{nykvist}$ Cen A')
ylabel('correlation')
legend()

#da="centauriA1.dat"
#da="kepler1.dat"
#da="data0.dat"
#-----------------------------------------------------------------------------------------
da="centaurib.dat"
[x,y,z]=opendata.opendata(data=da)
y=submean.submean(y)
for i in range(len(x)):
    y[i]=float(y[i])
    x[i]=float(x[i])*(3600*24)
    z[i]=1/float(z[i])**2

nykvist=1/(2*(x[2]-x[1]))
print nykvist
[y]=aband.aband(x,y,z,num,0.1*nykvist,nykvist,2,0.4*nykvist,0.4*nykvist)
[f,p,a,b]=aft.aft(x,y,z,0.1*nykvist,nykvist,num)
f=multiply(1000,f)
subplot(3,3,7)
qq=[]
uu=[]
for i in range(10,len(f)/20): 
 qq.append(auto.auto(f,p,i))
 uu.append(i*(f[2]-f[1])) 
plot(uu,qq)
title('Low-pass 0.1-0.4 $f_{nykvist}$ Cen B')
xlabel('mHz')
ylabel('correlation')
legend()

[x,y,z]=opendata.opendata(data=da)
y=submean.submean(y)
for i in range(len(x)):
    y[i]=float(y[i])
    x[i]=float(x[i])*(3600*24)
    z[i]=1/float(z[i])**2

nykvist=1/(2*(x[2]-x[1]))
print nykvist
[y]=aband.aband(x,y,z,num,0.1*nykvist,nykvist,3,0.4*nykvist,0.7*nykvist)
[f,p,a,b]=aft.aft(x,y,z,0.1*nykvist,nykvist,num)
f=multiply(1000,f)
subplot(3,3,8)
qq=[]
uu=[]
for i in range(10,len(f)/20): 
 qq.append(auto.auto(f,p,i))
 uu.append(i*(f[2]-f[1])) 
plot(uu,qq)
title('Band-pass 0.4-0.7 $f_{nykvist}$ Cen B')
xlabel('mHz')
ylabel('correlation')
legend()

[x,y,z]=opendata.opendata(data=da)
y=submean.submean(y)
for i in range(len(x)):
    y[i]=float(y[i])
    x[i]=float(x[i])*(3600*24)
    z[i]=1/float(z[i])**2

nykvist=1/(2*(x[2]-x[1]))
print nykvist
[y]=aband.aband(x,y,z,num,0.1*nykvist,nykvist,1,0.7*nykvist,0.7*nykvist)
[f,p,a,b]=aft.aft(x,y,z,0.1*nykvist,nykvist,num)
f=multiply(1000,f)
subplot(3,3,9)
qq=[]
uu=[]
for i in range(10,len(f)/20): 
 qq.append(auto.auto(f,p,i))
 uu.append(i*(f[2]-f[1])) 
plot(uu,qq)
title('High-pass 0.7-1$f_{nykvist}$ Cen B')
xlabel('mHz')
ylabel('correlation')
legend()



savefig('poAB.ps')
show()

