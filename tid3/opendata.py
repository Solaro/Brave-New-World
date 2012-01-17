#file that opens the data
#!~/tidsseriedata/data
def opendata(data=None):
 fline=[]
 f=open(data,"r")
#read line into array
 flist=f.readlines()
 x=[]
 y=[]
 z=[]
 b=len(flist[10].split())
 print b
 if b==2:
  z=None
  for i in range(7,len(flist)-2):#range(len(flist)-1)
   a=flist[i].split()
   x.append(a[0])
   y.append(a[1])
  return [x,y,z]
 elif b==3:
  for i in range(10,len(flist)-3):#range(len(flist)-1)
   a=flist[i].split()
   x.append(a[0])
   y.append(a[1])
   z.append(a[2])
  return [x,y,z]
