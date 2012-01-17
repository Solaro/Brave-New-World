#script der tager data og analyserer dem.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pylab as mplot
import opendata
import aft
import submean
from numpy import *
import aband
import aclean
import awindow
import auto
da="centaurib.dat"
#da="sol.dat"
path="pictures/"
num=7000
#da="centauriA1.dat"
#da="kepler1.dat"
#da="data0.dat"
[x,y,z]=opendata.opendata(data=da)
y=submean.submean(y)
for i in range(len(x)):
    y[i]=float(y[i])
    x[i]=float(x[i])*(3600)*24
    z[i]=1/float(z[i])**2
#z=None
nykvist=1/(2*(x[2]-x[1]))
print nykvist
#[y,f]=aband.aband(x,y,1000,z,0.0001,0.0021,3,0.0005,0.0015)
[y]=aband.aband(x,y,z,num,0.1*nykvist,nykvist,3,0.0040,0.0045)
[f,p,a,b]=aft.aft(x,y,z,0.1*nykvist,nykvist,num)
f=multiply(1000,f)

qq=[]
uu=[]
for i in range(10,len(f)/10): 
 qq.append(auto.auto(f,p,i))
 uu.append(i*(f[2]-f[1]))

indexvalue=[] 
lv=0#qq[0]
for i in range(len(qq)):
 if qq[i] > lv and uu[i]>0.08 and uu[i]<0.2:
  lv=qq[i]
  indexvalue=i
  print i
print uu[indexvalue]


mplot.plot(uu,qq,label="Powerspectrum for the Sun")
#mplot.legend(loc="upper left")
mplot.title(r"Correlation of the powerspectrum for Cen B $[4.0-4.5]mHz$")
mplot.xlabel(r"$\Delta$ f [mHz]")
mplot.ylabel(r"Correlation")
mplot.savefig(path+"Cb-cor-int3")
mplot.show()


