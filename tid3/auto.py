#autocorrelation
from numpy import *
def auto(f,p,dT):
	N=len(f)
	at=1/float(N-dT)*dot(p[dT:],p[0:(N-dT)])
	return at
