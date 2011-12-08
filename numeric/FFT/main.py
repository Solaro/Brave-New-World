# The testing file for the dft function
import math
import fft
import matplotlib.pyplot as pyp
import time

num=100
x=[i*1.0/num*4*math.pi for i in range(num)]
fun=[math.sin(x[i])/1.6+math.cos(x[i]/3)+math.cos(x[i]*4)/3 for i in range(len(x))]


sign=1
a=fft.fft(fun,sign)
b=fft.invftt(a,sign)

pyp.figure(1)
pyp.title('The fast fourier transform F(x)')
pyp.plot(x, fun,'b',label='$f(x)=sin(x)/6+cos(4x)/3+cos(x/3)$')

pyp.plot(x, b,'r-.',label='$f(x)=F^{-1}(F(f(x)))$')
pyp.legend()
pyp.savefig('Trigonometric.png',format='png')


num=1000
x=[i/1000.0 for i in range(num)]#[i./num for i in range(num)]
fun=[0.25/((i-0.5)**2+0.25) for i in x]

sign=1
a=fft.fft(fun,sign)
b=fft.invftt(a,sign)

pyp.figure(2)
pyp.title('The fast fourier transform F(x)')
pyp.plot(x, fun,'b',label='$f(x)=0.25/((x-0.5)^2+0.25)$')

pyp.plot(x, b,'r--',label='$f(x)=F^{-1}(F(f(x)))$')
pyp.legend()
pyp.savefig('Lorenzian.png',format='png')
