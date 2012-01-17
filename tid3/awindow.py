#window funktionen
import math
import aft
from numpy import *
def awindow(x,z,f):
    dx=abs(x[1]-x[0])
    dfrek=(f[1]-f[0])
    fnykvist=float(1)/(2*dx)
    fx=multiply(0.5*fnykvist,x)
    ysin=sin(2*pi*fx)
    ycos=cos(2*pi*fx)
    total=float(fnykvist)/dfrek
    num=int(round(0.90*total))
    a=float(0.5*fnykvist-total*dfrek*0.45)
    b=float(0.5*fnykvist+total*dfrek*0.45)
    [f,psin,ee,rr]=aft.aft(x,ysin,None,a,b,num)
    [f,pcos,a,b]=aft.aft(x,ycos,None,a,b,num)
    rr=add(psin,pcos)
    rk=rr.sum()
    return 0.5*rk
 
