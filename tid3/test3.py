#script der tager data og analyserer dem.


import opendata
import aft
import submean
from pylab import *
from numpy import *
import aband
import aclean
import awindow
import auto
subplots_adjust(hspace=0.4)
da="centauria.dat"#"sol.dat"
num=1000
#da="centauriA1.dat"
#da="kepler1.dat"
#da="data0.dat"

x=linspace(1,10,10)
y=x**2

plot(x,y)

show()
