import math
import lsfit
import matplotlib.pyplot as pyp

# Defining the polynomial function
num=15
x=range(num)
y=[]
dy=[]
for i in x:
	y.append(5+2*i+1./7*i**2-1./33*i**3+1./747*i**4)
	dy.append(1)
# Defining the Lorenzian function
num=100
x1=range(num)
y1=[]
dy1=[]
for i in x1:
	y1.append(50./((i-50)**2+50))
	dy1.append(1)

#Defining the functions which can by fittet to
f1 = lambda x:1; f2 = lambda x:x; f3 = lambda x:x**2; f4 = lambda x:x**3
funs=[f1,f2,f3,f4]

#Making the least-square fit
[c,S]=lsfit.lsfit(x,y,dy,funs)
[c1,S1]=lsfit.lsfit(x1,y1,dy1,funs)

z=[]
for i in x:
	z.append(c[0]*f1(i)+c[1]*f2(i)+c[2]*f3(i)+c[3]*f4(i))

z1=[]
for i in x1:
	z1.append(c1[0]*f1(i)+c1[1]*f2(i)+c1[2]*f3(i)+c1[3]*f4(i))

#Representing the results

pyp.figure(1)
pyp.plot(x,y,label="data from $f(x)=5+2x+1/7x^2-1/33x^3+1/474x^4$")
pyp.plot(x,z,label="fittet by $f(x)=a+bx+cx^2+dx^3$")
pyp.title("4-order polynomial")
pyp.legend()
pyp.savefig('poly_fit_of_poly.png',format='png')
pyp.figure(2)
pyp.plot(x1,y1,label="data from $f(x)=25/((x^2-50)+25)$")
pyp.plot(x1,z1,label="fittet by $f(x)=a+bx+cx^2+dx^3$")
pyp.title("Lorenzian function")
pyp.legend()
pyp.savefig('poly_fit_of_lorentzian.png',format='png')

print 'The square roots of the diagonal elements from the covariance matix'
print 'from the first ploynomial fit'
sigma=[]
for i in range(len(c)):
	sigma.append((S[i][i])**0.5)
print 'a='+str(c[0])+'+-'+str(sigma[0])+', b='+str(c[1])+'+-'+str(sigma[1])+', c='+str(c[2])+'+-'+str(sigma[2])+', d='+str(c[3])+'+-'+str(sigma[3]) 
print 'from the second Lorenzian fit'
sigma=[]
for i in range(len(c)):
	sigma.append((S1[i][i])**0.5) 
for i in range(len(c)):
	sigma.append((S[i][i])**0.5)
print 'a='+str(c[0])+'+-'+str(sigma[0])+', b='+str(c[1])+'+-'+str(sigma[1])+', c='+str(c[2])+'+-'+str(sigma[2])+', d='+str(c[3])+'+-'+str(sigma[3]) 


