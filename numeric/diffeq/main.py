import matplotlib.pyplot as pyp
import math
import diffsolver
x=[0]
b=5*math.pi
y=[[0,1]]
h=0.5
acc=0.01
eps=0.0
ncalls=0

def func(x,y):
 return [y[1],-y[0]]

[xlist,ylist]=diffsolver.rkdrive(func,x,y,b,acc,eps,h)
w=len(x)
z=[]
for i in range(w):
 z.append(y[i][0])

pyp.figure(1)
pyp.plot(x,z)
pyp.title("Differeltialeq $df(x)/dx =-f(x)$, $x_{start}=0$")
pyp.show()

#for i in range(len(x)):
# print repr(x[i]).rjust(2), repr(z[i]).rjust(3)


