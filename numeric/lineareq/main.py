import qr

A=qr.randomm(3,3)
print 'The start matrix'
print '------A-------'
print A
print '--------------'
b=qr.randomm(3)
print 'Choose the vector b='+str(b)
print 'Make the QR-decomposition'
[Q,R]=qr.qrdec(A)
print '------Q-------'
print Q
print '--------------'
print '------R-------'
print R
print '--------------'
x=qr.qrback(Q,R,b)
print 'Make the backward substitution to solve Ax=b. x='
print x
print 'The determinant of Q'
print qr.det(Q)
print 'The determinant of R'
print qr.det(R)
print 'The determinant of A'
print qr.det(A)
print 'The inverse of A'
print qr.inv(A)


