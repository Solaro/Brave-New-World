def bins(x,z):
    a=len(x)/2
    i=0
    j=len(x)
    while (j-i)>1:
        if z>x[a]:
            i=a
        else:
            j=a
        a=(i+j)/2
    return [i,j]
