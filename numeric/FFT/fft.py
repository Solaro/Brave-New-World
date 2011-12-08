import cmath
#cmath supports the use of complex numbers

def dft(data,sign):
 n=len(data)
 c=range(n)
 w=cmath.exp(sign*2*cmath.pi*complex(0,1)/n)
 for i in range(n):
  c[i]=0
  for h in range(n):
   c[i]=c[i]+data[h]*w**(h*i)
  c[i] = c[i]/cmath.sqrt(n)
 return c

def fft(data,sign):
 n=len(data)
 if n%2==0:
  e=cmath.exp(sign*2*cmath.pi*complex(0,1)/n)
  m=int(n/2)
  c=range(n)
  ceven=fft([data[2*i] for i in range(m)],sign)
  codd=fft([data[2*i+1] for i in range(m)],sign)
  for i in range(m):
   c[i]=(ceven[i]+e**i*codd[i])/(2**0.5)
   c[i+m]=(ceven[i]-e**i*codd[i])/(2**0.5)
 else:
  c=dft(data,sign)
 return c

def invftt(data,sign):
 return fft(data,-sign)
