import math
def rkstep(func,x,y,h):
 k0=func(x,y)
 a=len(y)
 y12=[0,0]
 y1=[0,0]
 dy=[0,0]
 for i in range(a):
  y12[i]=y[i]+k0[i]*h/2
 k12 = func(x+h/2,y12)
 for i in range(a):
  y1[i]=y[i]+k12[i]*h
 for i in range(a):
  dy[i]=(k12[i]-k0[i])*h/2
 return [y1,dy]
 
def rkdrive(func,xlist,ylist,b,acc,eps,h):
 ee=[1,2,3]
 a=xlist[0]
 x=xlist[len(xlist)-1]
 y=ylist[len(ylist)-1] 
 if x==b:
  return [xlist,ylist]
 if (x+h) > b:
  h=b-x
 [y1,dy]=rkstep(func,x,y,h)
 err=norm(dy)
 tol=(norm(y1)*eps+acc)*math.sqrt(float(h)/(b-a))
 if err > 0:
  new_h=h*(tol/err)**(0.25)*0.95
 else:
  new_h = 2*h
 if tol>err:
  xlist.append(x+h)
  ylist.append(y1)
  a = rkdrive(func,xlist,ylist,b,acc,eps,new_h)
  return a 
 else:
  a = rkdrive(func,xlist,ylist,b,acc,eps,new_h)  
  return a

def norm(v):
 return math.sqrt(v[0]*v[0]+v[1]*v[1])
