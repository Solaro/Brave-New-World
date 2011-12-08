import qtspline
import matplotlib.pyplot as pyp
intervalstart=-5
intervalslut=5
points=8
x=[intervalstart+i*(intervalslut-intervalstart)*1.0/(points-1) for i in range(points)]
y=[1.0/(1.0+i**2) for i in x] #Lorenz function centered at zero
interpolationpoints=100
xinter=[intervalstart+i*(intervalslut-intervalstart)*1.0/(interpolationpoints-1) for i in range(interpolationpoints)]
b=[]
for k in xinter:
 b.append(qtspline.pinterp(x,y,k))

[a,c]=qtspline.linterpol(x,y,interpolationpoints)
[u,s]=qtspline.qinterpol(x,y,interpolationpoints)

# plot the datapoints and the interpolated data
pyp.figure(1)
pyp.plot(xinter,b,label="polynomial interpolation")
pyp.plot(a,c,label="linear spline")
pyp.plot(u,s,label="quadratic spline")
pyp.plot(x,y,'ro',label="data points from the Lorentz function")
ax = pyp.axis([-5, 5, 0, 1.3])
pyp.title("Lorentz-function")
pyp.legend()
pyp.savefig('example1.png',format='png')
intervalstart=-5
intervalslut=5
points=1000
x=[intervalstart+i*(intervalslut-intervalstart)*1.0/(points-1) for i in range(points)]

y=[]
for i in x:
 k=0
 if abs(i+4)<0.5:
  k=1
 if abs(i+2)<0.5:
  k=1
 if abs(i+0)<0.5:
  k=1
 if abs(i-2)<0.5:
  k=1
 if abs(i-4)<0.5:
  k=1
 y.append(k)

interpolationpoints=1000
[a,b]=qtspline.qinterpol(x,y,interpolationpoints)
pyp.figure(2)
pyp.plot(x,y,label="step-function")
pyp.plot(a,b,label="quad interpolation")
ax = pyp.axis([-5, 5, 0, 2])
pyp.legend()
pyp.title("quadratic interpolation")
pyp.savefig('example2.png',format='png')



