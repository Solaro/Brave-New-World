from pylab import *
from numpy import *
def transfilter(x,y,snum,deltas,antal):
	D=empty((antal,len(y)))
	for i in range(antal):
		B=snum+deltas
		for j in range(len(y)-3*B):
		up0=sum(y[i:i+B])
		do=sum(y[i+B:i+2*B])
		up1=sum(y[i+2*B:i+3*B])
		D[i,j]=do-(up0+up1)/2
	return D
			
	
	
