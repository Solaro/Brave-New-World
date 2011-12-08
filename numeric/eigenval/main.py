#main

import jacobi

M=[[3,1],[1,7]]
print 'matrix som diagonaliseres'
print M
[A,V,c] = jacobi.jacobi(M)
print 'egenvaerdierne'
print A
a1=5+5**0.5
a2=5-5**0.5
print 'The precise eigenvalues are 5+-sqrt(5)='+str(a2)+', '+str(a1)
print 'number of sweeps'
print c
print 'with eps of 1e-12'
M=[[1,2,3],[2,4,-5],[3,-5,6]]

print 'matrix som diagonaliseres'
print M
[A,V,c] = jacobi.jacobi(M)
print 'egenvaerdierne'
print A
print 'antallet af sweeps'
print c
