#By a mcmc I will try to sample a sin(x)^2 on the interval [0,2pi]
import math
import rosenbrock
import random
import histogram
import histo
# assume the testfunction is two-dimensional
def daserste(num,xstartpoint,ystartpoint):
	#print '------------'
	#print testfun.testfun(3)
	#print '------------'
	#num=50000
	#x=(range(num)/num-1./4)*20
	#P=math.exp(abs(x))*abs(2*x**2+7*x**3+x)/(x**2+2)

	#Have genetated the function wich can be sampled from
	datalength=10000
	datamean=4
	datasigma=2
	aa=0
	data=[]
	while aa < datalength:
		data.append(random.gauss(datamean,datasigma))
		aa+=1
	# Lav histogram for data:
	interval=[min(data),max(data)]
	numbin=100
	deltabin=(max(data)-min(data))/100
	a,b=histo.histo(data,interval,deltabin,numbin)
	#for i in range(len(a)):
	#	print repr(a[i]).rjust(1), repr(b[i]).rjust(2)

	#The monte carlo step
	k=0
	xs=[]
	ys=[]
	Pxs=[]
	#Initial starting value
	x=xstartpoint
	y=ystartpoint
	aa=0
	kk=len(data)
	newdata=[]
	while aa < kk:
		newdata.append(random.gauss(x,y))
		aa+=1
	anew,bnew=histo.histo(newdata,interval,deltabin,numbin)

	Px=0
	for i in range(len(anew)):
		Px+=(a[i]-anew[i])**2	
	#Px=rosenbrock.rosenbrock(x,y)#math.exp(-abs(x))*abs(2*x**2+7*x**3+x)/(x**2+2)#testfun.testfun(x)
	xs.append(x)
	ys.append(y)
	Pxs.append(Px)
	#Step
	while k < num:
		steplength=0.1
		xn=(random.random()-1./2)*2
		yn=(random.random()-1./2)*2
		xny=x+(xn/(xn**2+yn**2)**0.5)*steplength
		yny=y+(yn/(xn**2+yn**2)**0.5)*steplength 
		aa=0
		kk=len(data)
		newdata=[]
		while aa < kk:
			newdata.append(random.gauss(xny,yny))
			aa+=1
		anew,bnew=histo.histo(newdata,interval,deltabin,numbin)
		Pxny=0
		for i in range(len(anew)):
			Pxny+=(a[i]-anew[i])**2	
		#print '--------'
		#print Pxny
		#print 'Px'
		#print Px
		#Pxny=rosenbrock.rosenbrock(xny,yny)#math.exp(-abs(xny))*abs(2*xny**2+7*xny**3+xny)/(xny**2+2)#testfun.testfun(x)
		if Pxny < Px: #max Pxny > Px
		#print 1
			x=xny
			y=yny
			Px=Pxny
		else:
		
			auk=random.random()
			b=Px/Pxny #max Pxny/Px
		#print b
		#print a
			if b > auk:
				x=xny
				y=yny
				Px=Pxny
			#print 2
		xs.append(x)
		ys.append(y)
		#print Px#.append(Px)
		k+=1
	
	return xs,ys
	#for i in range(len(xs)):
	#print repr(xs[i]).rjust(1), repr(Pxs[i]).rjust(2)


