def submean(y):
 sumy=0
 l=len(y)
 for k in range(l):
  sumy+=float(y[k])
 M=sumy/len(y)
 for i in range(l):
  y[i]=float(y[i])-M
 return y
