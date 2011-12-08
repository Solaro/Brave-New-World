#QR-decomposition
import math
import random

def randomm(*dim):
 """Generates a random matrix of variable size (x,y,z,..) with elements between 0 and 1"""
 if len(dim) == 0:
   return random.random()
 row = dim[0]
 col = dim[1:]
 return [randomm(*col) for i in xrange(row)]


def dot(a,b):
 """Defines the dotproduct between vectors"""
 s=0
 for i in xrange(len(a)):
  s+=a[i]*b[i]
 return s 

def zeros(*dim):
 """Generates a zero matrix of variable size (x,y,z,..)"""
 if len(dim) == 0:
   return 0
 row = dim[0]
 col = dim[1:]
 return [zeros(*col) for i in xrange(row)]

def dim(A):
 """Returns the dimensions e.g. the number of times a nested list is nested"""
 i=0
 try:
  while(True):
   A=A[0]
   i+=1
 except Exception:
  pass
 return i
	
def copy(A):
 """Copies the dataelements of a nested list (matrix)"""
 if dim < 1:
  print 'dimension is undefined and copy passes'
  pass
 if dim(A)==1:
  return A[:]
 return [copy(c[:]) for c in A]

def inv(A):
 """Calculates the inverse matrix of the matrix given"""
 [Q,R]=qrdec(A)
 a=len(A)
 Ai=zeros(a,a)
 b=zeros(a)
 for i in xrange(len(A)):
   b[i]=1
   x=qrback(Q,R,b)
   b[i]=0
   Ai[i][:]=x
 return Ai

def qrback(Q,R,b):
 """The QR back substitution"""
 m=len(Q)
 c=[0]*m
 x=[0]*m
 for i in xrange(m):
  for k in xrange(len(b)):
   c[i]+=Q[i][k]*b[k]
  for ii in xrange(m):
   i=m-1-ii
   s=0
   for k in xrange(i+1,m):
    s+=R[k][i]*x[k]
   x[i]=(c[i]-s)/R[i][i]
 return x

def qrdec(A):
 """The QR-decomposition of a quadratic matrix A"""
 m=len(A)
 Q=copy(A)
 R=zeros(m,m)
 for i in xrange(m):
  e=Q[i]
  r=math.sqrt(dot(e,e))
  if r == 0:
   print 'singular matrix'
  R[i][i]=r
  for k in xrange(len(e)):
   e[k]/=r
  for j in xrange(i+1,m):
   q=Q[j]
   s=dot(e,q)
   for k in xrange(len(q)):
    q[k]-=s*e[k]
   R[j][i]=s  
 return [Q,R]

def det(W):
 """Returns the determinant of given matrix"""
 [Q,R]=qrdec(W)
 det = 1
 for i in xrange(len(W)):
  det*=R[i][i]
 return det
