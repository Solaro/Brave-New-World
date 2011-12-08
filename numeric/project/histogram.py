import math
import random
import rosenbrock
import ddassam
class histogram(object):
	"""Documentation for the histogram class: """

	def __init__(self,x,interval,deltabin,numbin,vector,vecnum):
		self.x = x
		self.interval = interval
		self.deltabin = deltabin
		self.numbin = numbin 
		self.vector = vector
		self.vecnum = vecnum
		self.hisvector,self.hiscount = self.histo2(x,interval,deltabin,numbin)
		self.xcoord,self.ycoord,self.zcoord = self.histoadd()
		
		pass
	# Make points into a histogram
	# Input: takes vector x
	# Interval: A vector where the first and last points are set as endpointd 	for the histogram
	# deltabin: length of each bin
	# numbin: number of bins
	def histo2(self,x,interval,deltabin,numbin):
		dim=len(interval)
		l=len(x[0][:])
		w=[];start=[];stop=[];hisvector=[];hiscount=[]
		start = [a[0] for a in interval]
		stop = [a[1] for a in interval]
		#start=interval[:][0]
		#stop=interval[:][1]
		#print 'start'
		#print x
		#print 'stop'
		#print stop
		w=[0]*dim
		hisvector = [[0]*numbin]*dim
		hiscount = [] 
		hislist = [0]*numbin**dim#[[0]*dim]*numbin
		for j in range(dim):
			for i in range(numbin):
				u=(stop[j]-start[j])*float(i)/(numbin-1)+start[j]
				hisvector[j][i]=u
		for i in range(l): # number of intrences in x
			for j in range(dim): # number of dimensions
				k=0
				if x[j][i] > start[j] and x[j][i] < stop[j]:
					a=int((x[j][i]-start[j])/deltabin) 
					w[j]=a
			hiscount.append(w[:])
		
		
		return hisvector, hiscount


	# From a set of coordiantes [x1,x1,..]
	def vectorlin(self,dim=[], coord=[]):
		step = 1
		for i in dim[0:-1]:
			step=step*i
		point=0
		j=1
		dim.append(1)
		for i in coord:
			point+=step*i
			step = step/dim[j]
			j+=1
		dim.pop()
		return point


	def vectorinvlin(self,dim=[], arraynumber=[]):
		point=[0]*len(dim)
		j=1
		step = 1
		for i in dim[0:-1]:
			step=step*i
		dim.append(1)
		for i in dim[0:-1]:
			point[j-1] = int(arraynumber/step)
			arraynumber = arraynumber%step
			step = step/dim[j]

			j+=1
		dim.pop()
		return point

	def histoadd(self):#,hiscount,hisvector
		val=[500,500]
		vecnumb=[0,1]
		# val are the values in the n-dim parameterspace wich the histogram 
		# is created from
		# vecnumb are the 2 parameters for wich the histogram is plottet
		# hisvecnumb is the number of the two histogram vectors plottet
		# Make a 0 vector to count in

		hiscount=self.hiscount
		hisvector=self.hisvector
		
		dim=len(hiscount[0][:])
		hlen=len(hisvector[0][:])
		count = [0]*hlen**dim
		dims = [hlen]*dim
		# To create a matrix (wich I properly will not do)
		#It is possible to define a anonomous function 	
		#g = lambda x,dim: [x]*dim
		# I wan't to call the function recursively
		#hist=[0]*len(hisvector)
		#number = 1
		#while number < dim:
		#	hist= g(hist,len(hisvector))
		#print len(count)
		for i in range(len(hiscount)):
			numb = self.vectorlin(dim = dims, coord = hiscount[i])
			count[numb] += 1
		# val is the point where the i, and j has to be changed		
		xcoord=[]
		ycoord=[]
		zcoord=[]		
		coord = val[:]
		for i in range(len(hisvector[0][:])):
			for j in range(len(hisvector[0][:])):	
				for k in range(len(val)):
					if k == vecnumb[0]: 
						coord[k]=i
					if k == vecnumb[1]:
						coord[k]=j
				
				num = self.vectorlin(dim = dims, coord = coord)
				#xcoord.append(hisvector[vecnumb[0]][i])
				#ycoord.append(hisvector[vecnumb[1]][j])
				xcoord.append(hisvector[0][i])
				ycoord.append(hisvector[1][j])
				zcoord.append(count[num])
				#print repr(hisvector[vecnumb[0]][i]).rjust(1), repr([vecnumb[1]][j]).rjust(2), repr(count[num]).rjust(3)
		#print hisvector[0][300]
		#print xcoord
		return xcoord,ycoord,zcoord
					
if __name__=='__main__':
	print 'tralala1'	
	a = histogram.histogram(x,interval,deltabin,numbin)
	b = a.sq()
#	[hisvector,hiscount]=
	#Assume one string of numbers to make the histogram from
