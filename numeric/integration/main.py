import adp
import f
import f1
import f2
import f3
import math
[a,b]=adp.adp(0,1,1e-3,1e-3,f)
print 'integralet af log(x)/sqrt(x) fra 0 til 1 er'
print a
print 'med usikkerheden'
print b
print 'der blev foreteget 62 itterative funktionskald'

[a,b]=adp.adp(0,1,1e-10,1e-10,f1)
print 'integralet af 4*sqrt(1-(1-x)^2) fra 0 til 1 er'
print a
print 'med usikkerheden'
print b
print 'der blev foreteget 2871 itterative funktionskald'

[a,b]=adp.adp(0,1,1e-5,1e-5,f2)
print 'integralet af sin(1000*x)*cos(2000*x) fra 0 til 1 er'
print a
print 'med usikkerheden'
print b
print 'der blev foreteget 3176 itterative funktionskald'

[a,b]=adp.adp(0,1,1e-8,1e-8,f2)
print 'integralet af exp(-x^2) som er sqrt(pi)/2*errorfunctionen fra 0 til 1 er'
print a
print 'med usikkerheden'
print b
print 'der blev foreteget 175 itterative funktionskald'

