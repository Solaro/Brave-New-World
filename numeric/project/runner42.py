import unittest
import hist2d as histo2
import ddassam
import rosenbrock
import random
import histogram
import daserste
#number of elements entering into the sampling
sampnum=50
#The sampling id from the function testfun1.
#To use another function e.g. testfun42 then import test42 and pass test42 
#as the last argument 
xstartpoint = random.random()#-random.random()
ystartpoint = random.random()#-random.random()
#The point where the sampling starts
#[x,y] = ddassam.dis2sam(sampnum,xstartpoint,ystartpoint,rosenbrock)
[x,y] = daserste.daserste(sampnum,xstartpoint,ystartpoint)
t=[x,y]
# The Histogram:
# Binsize
binsize=0.1
# Binnumber
numbin=200
# Interval
interval=[[-10,10],[-10,10]]
#where t is the sampling from the function
k=[0,1]
a=histogram.histogram(t,interval,binsize,numbin,2,k)
#print(len(a.hisvector))
#print(len(a.hisvector)**2)
#print(len(a.xcoord))


#for i in range(len(a.hiscount)):
#	print repr(a.hiscount[i][0]).rjust(1), repr(a.hiscount[i][1]).rjust(2)

#print(a.hiscount)
knu=0
for i in range(len(a.xcoord)):
	if i%len(a.hisvector[0][:]) == 0:
		print '     '
#	k=a.zcoord[i]
#	if k > knu:
#		x=a.xcoord[i]
#		y=a.ycoord[i]
#		knu=k 
	print repr(a.xcoord[i]).rjust(1), repr(a.ycoord[i]).rjust(2), repr(a.zcoord[i]**0.5).rjust(3)
#print x,y
# To normalize thehistogram
#--for i in range(len(tes)):
#--	tes[i]=tes[i]*1./(sampnum*binsize)
# The tes (number of counts in each bin in the histogrem) 
# and tus (the vector the specifies the bins) is printed 
#for i in range(len(tes)):
#	for j in range(len(tes)):
#		
#print x
#print '------------------'
#print y
#for i in range(len(x)):
#	print repr(x[i]).rjust(1), repr(y[i]).rjust(2)
