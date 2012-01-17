import awindow
import aft
import bins
from numpy import *
def aband(x,y,z,antal,frekmin,frekmax,btype,fmin,fmax=None):
    #highpass
    if btype==1:
        [frek,p,a,b]=aft.aft(x,y,z,frekmin,frekmax,antal)
        [c,d]=bins.bins(frek,fmin)        
        wp=awindow.awindow(x,z,frek)
        for j in range(len(y)):
            for i in range(d):
                y[j]=y[j]-(a[i]*sin(2*pi*frek[i]*x[j])+b[i]*cos(2*pi*frek[i]*x[j]))/(wp)
        return [y]
    #lowpass
    elif btype==2:
        [frek,p,a,b]=aft.aft(x,y,z,frekmin,frekmax,antal)
        [c,d]=bins.bins(frek,fmin)  
        wp=awindow.awindow(x,z,frek)
        for j in range(len(y)):
            u=0
            for i in range(c):
                u+=a[i]*sin(2*pi*frek[i]*x[j])+b[i]*cos(2*pi*frek[i]*x[j])
            y[j]=u/(wp)
        return [y]
    #bandpass
    else:
        [frek,p,a,b]=aft.aft(x,y,z,frekmin,frekmax,antal)
        [c,d]=bins.bins(frek,fmin)
        [e,f]=bins.bins(frek,fmax)
        wp=awindow.awindow(x,z,frek)
        for j in range(len(y)):
            u=0
            for i in range(c,f):
                u+=a[i]*sin(2*pi*frek[i]*x[j])+b[i]*cos(2*pi*frek[i]*x[j])
            y[j]=u/float(wp)
        return [y]




