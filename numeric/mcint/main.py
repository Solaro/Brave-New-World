import mcr
import f1
import f2
import math
pi=math.pi
a=[0,0,0]
b=[pi,pi,pi]
dim=3
N=int(1e7)
[a,b]= mcr.mcr(a,b,0.5,N,f1,dim)
print 'montecarlo integration af 1/(1-cos(x)cos(y)cos(z)) hvor x,y,z tilhoerer intervalet fra 0 til pi'
print a
print 'med usikkerheden'
print b


a=[-1,-1,-1]
b=[1,1,1]
dim=3
N=int(1e5)
[a,b]= mcr.mcr(a,b,0.5,N,f2,dim)
print 'montecarlo integration af sin(sin(x^2)+sin(y^2)+sin(z^2)) hvor x,y,z tilhoerer intervalet fra -1 til 1'
print a
print 'med usikkerheden'
print b


