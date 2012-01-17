
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
#da="centaurib.dat"
#da="sol.dat"
path="pictures/"
num=7000
#da="centauriA1.dat"
da="kepler2sim.dat"
#da="realkepler.dat"
#da="data0.dat"
[x,y,z]=opendata.opendata(data=da)
y=submean.submean(y)


for i in range(len(x)):
    y[i]=float(y[i])
    x[i]=float(x[i])#*(3600)*24
#    z[i]=1/float(z[i])**2


z=None
nykvist=1/(2*(x[2]-x[1]))
print nykvist
#[y,f]=aband.aband(x,y,1000,z,0.0001,0.0021,3,0.0005,0.0015)
#[y]=aband.aband(x,y,z,num,0.1*nykvist,nykvist,3,0.0040,0.0045)
#[f,p,a,b]=aft.aft(x,y,z,0.1*nykvist,nykvist,num)
#f=multiply(1000,f)

for i in range(len(x)):
 if y[i]< -5000:
  y[i]=(y[i-1]+y[i+1])/2
y=submean.submean(y)
qq=[]
uu=[]
#for i in range(10,len(f)/10): 
# qq.append(auto.auto(f,p,i))
# uu.append(i*(f[2]-f[1]))

#indexvalue=[] 
#lv=0#qq[0]
#for i in range(len(qq)):
# if qq[i] > lv and uu[i]>0.08 and uu[i]<0.2:
#  lv=qq[i]
#  indexvalue=i
#  print i
#print uu[indexvalue]

#the filter thing
stt=[]

i=5
tf=[]
for j in range(len(x)-4*i):
 j=j+2*i
 tf.append(mean(y[j-int(0.5*i):j+int(0.5*i)])-(mean(y[j-int(1.0*i):j-int(0.5*i)-1])+mean(y[j+int(0.5*i):j+int(1.0*i)+1]))/2)
for j in range(len(tf)):
 tf[j]=tf[j]*tf[j]*tf[j]
xny=x[2*i:(len(x)-2*i)]
for i in range(len(xny)):
 xny[i]=xny[i]/(24)

a=0
for i in range(len(tf)):
 if tf[i]> tf[a]:
  a=i
print'-------------------------------'
print tf[a]
print '------------------------------'
b=0
for i in range(a-4):
 if tf[i]> tf[b] and abs(i-a)>7:
  b=i
print (xny[a]-xny[b])
for i in range(4,len(tf)-10):
 qq.append(auto.auto(xny,tf,i))
 uu.append(i*(xny[2]-xny[1]))
c=0
for i in range(len(qq)):
 if qq[i]>qq[c]:
  c=i
#for j in range(len(qq))
# qq[j]=qq[j]*qq[j]*qq[j]
#print 'tra lala'
#print uu[c]/6*365
#[f,p,l,k]=aft.aft(xny,tf,None,1,10000,10000)
#print f[:32]
#print p[:32]
#for i in range(len(x)):
# x[i]=x[i]/365

#mplot.plot(f[:1200],p[:1200])

ee=len(uu)-150
mplot.plot(uu[:ee],qq[:ee],'-*')
mplot.ylim([0,1e-24])

#mplot.legend(loc="upper left")
mplot.title(r"Kepler-sim2 data")
mplot.xlabel(r" Time [days]")
mplot.ylabel(r"Correlation function for 10 hour filter")
mplot.savefig(path+"keplersim-sqr1")
mplot.show()


