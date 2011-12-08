import newton
import simplex
import math

print 'Solving the rootfinding with the Newton method'

f0 = lambda x: (x[0]-2)**2+ (x[1]+1)**2+(x[2]+3)**2
#def f0(x):
# return (x[0]-2)**2

def f1(x):
 return (x[1]+1)**2

def f2(x):
 return (x[2]+3)**2

fs=[f0,f1,f2]

u=newton.newton(fs,[1.5,-0.5,-5.2])
print 'Solving f=0 with f(x,y,z)=(x-2)^2+(y+1)^2+(z+3)^2, initial point (x,y,z)=[1.5,-0.5,-5.2] and acceptance 1e-6'
print u
print 'the function value at this point is'
print f0(u)


#banana example 

f0 = lambda x: (1-x[0])**2+100*(x[1]-x[0]**2)**2 
f1 = lambda x: (1-x[0])**2
fs=[f0,f1]
u=newton.newton(fs,[-1.3,2.7])
print 'Solving Rosenbruck'
print 'with f(x,y)=(1-x)^2+100*(y-x^2)^2, initial point (x,y)=[-1.3,2.7] and acceptance 1e-6'
print u
print 'the function value at this point is'
print f0(u)
#Himmelblau example

f0 = lambda x: (x[0]**2+x[1]-11)**2+(x[0]+x[1]**2-7)**2 
f1 = lambda x: (x[0]+x[1]**2-7)**2
fs=[f0,f1]
u=newton.newton(fs,[-1.3,2.7])

print 'Solving Himmelblau'
print 'with f(x,y)=(x^2+y-11)^2+(x+y^2-7)^2, initial point (x,y)=[-1.3,2.7] and acceptance 1e-6'
print u
print 'the function value at this point is'
print f0(u)

print 'Solving the equations (1-x)=0 and 10(y-x^2)=0 with initial point (x,y)=[-1.3,2.7]'
f0 = lambda x: (x[0]-1) 
f1 = lambda x: 10*(x[1]-x[0]**2)
fs=[f0,f1]
u=newton.newton(fs,[-1.3,2.7])
print u

#print f0(u)


print 'Solving the optimizing problems with the simplex'

f0 = lambda x: (x[0]-0.5)**2+(x[1]+1)**2
s=[[-1.5,-1.9],[1.5,1.5],[1.0,-1]]
#f0 = lambda x: (1-x[0])**2+100*(x[1]-x[0]**2)**2 

print 'Solving the equation f(x,y)=(x-0.5)^2+(y+1)^2'
print 'The starting simplex s=[[-1.5,-1.9],[1.5,1.5],[1.0,-1]] and acceptance 1e-2'
#The starting simplex

a=simplex.simplex(f0,s,1e-2)
pce=[0,0]
n=2
h=1

def reflect(pce,s,n):
 return [pce[i]+(pce[i]-s[h][i]) for i in range(n)]

def expand(pce,s,n):
 return [pce[i]+2*(pce[i]-s[h][i])for i in range(n)]

def contract(pce,s,n):
 return [pce[i]+0.5*(pce[i]-s[h][i]) for i in range(n)]

print 'The resulting point'
print a#contract(pce,s,n)


